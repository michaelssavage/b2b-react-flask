import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Navbar from '../components/Navbar';
import axios from "axios"
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import Button from "@material-ui/core/Button";

import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
    table: {
        minWidth: 650,
    },

    thCell: {
        color: "white",
        fontWeight: "bold",
    }
}));

function createData(product, orderID, date, quantity, edit) {
    return { product, orderID, date, quantity, edit };
}

export default function Orders() {

    const classes = useStyles();

    const [orders, setOrders] = useState([]);

    const user = { 
        customerID: document.cookie.slice(3)
    };
    
    const getOrder = async () => {
        try{
            const res = await axios.post(
                'http://localhost:5000/api/check_orders', 
                user
                );

            const productsArray = res.data;

            let orderList = [];
            for(let i = 0; i < productsArray.length; i++){

                orderList.push(createData(
                    productsArray[i]['product'],
                    productsArray[i]['orderID'],
                    productsArray[i]['date'],
                    productsArray[i]['quantity']
                ));
            }
            setOrders(orderList);
        
        }catch(err){
            console.error(err.message);
        }
    };

    useEffect(()=>{
        getOrder()},[]);

    const [open, setOpen] = useState(false);
    const [message, setMessage] = useState("");
    const [alertStyle, setAlertStyle] = useState("success");
    const handleMessage = (text, alert) => {
        setAlertStyle(alert);
        setMessage(text);
        setOpen(true);
    };
    
    const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
        return;
    }
    setOpen(false);
        };

    const deleteOrder = async (order) => {
        try{
            const res = await axios.post(
                'http://localhost:5000/api/delete_order', 
                {
                    customerID: user.customerID, 
                    orderID: order
                }
            );

            if (res.status === 200){
                handleMessage("Success, order successfully deleted", "success");
            }
        }catch(err){
            console.error(err.message);
            handleMessage("Error deleting order", "warning");
        }
    getOrder();
    };

    function RaisedButton(props) {
        return (
            <Button color="secondary" onClick={props.click}>
                Delete
            </Button>
        );
    }

    return (
        <>
            <Navbar />

            <Container component="main" maxWidth="xs" className="mt-5">  
                <Typography align="center" variant="h3"> 
                    My Orders
                </Typography>
            </Container>

            <Container component="main" maxWidth="md" className="mt-5">  
                <TableContainer component={Paper}>
                    <Table className={classes.table} aria-label="simple table">

                        <TableHead className= "table-color">
                        <TableRow>

                            <TableCell className={classes.thCell}>
                                Product Name
                            </TableCell>

                            <TableCell className={classes.thCell} align="center">
                                Order ID
                                </TableCell>

                            <TableCell className={classes.thCell} align="center">
                                Date Bought
                                </TableCell>

                            <TableCell className={classes.thCell} align="center">
                                Quantity Bought
                                </TableCell>

                            <TableCell align="right" className={classes.thCell}>
                                Delete Order
                                </TableCell>

                        </TableRow>
                        </TableHead>


                        <TableBody>
                        {orders.map((row) => (

                            <TableRow key={row.product}>
                                

                                <TableCell component="th" scope="row">
                                    {row.product}
                                </TableCell>

                                <TableCell align="center">
                                    {row.orderID}
                                </TableCell>

                                <TableCell align="center">
                                    {row.date}
                                </TableCell>

                                <TableCell align="center">
                                    {row.quantity}
                                </TableCell>

                                <TableCell align="right">

                                    <RaisedButton click={() => deleteOrder(row.orderID)} />

                                </TableCell>

                            </TableRow>
                        ))}
                        </TableBody>

                    </Table>
                </TableContainer>
            </Container>

            <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>

                <Alert onClose={handleClose} severity={alertStyle}>
                    {message}
                </Alert>
            </Snackbar>
        </>
    );
}