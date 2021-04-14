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
        customer_id: "user4"
    };
    
    const getOrder = async () => {
        try{
            const res = await axios.post(
                'http://localhost:5000/api/check_orders', 
                user
                );

            // console.log(res.data);

            const productsArray = res.data;
            // console.log(productsArray);

            let orderList = [];
            for(let i = 0; i < productsArray.length; i++){
                // console.log(productsArray[i]['customerID']);

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
        getOrder()},[])

    const deleteOrder = async (order) => {
        try{
            const res = await axios.post(
                'http://localhost:5000/api/delete_order', 
                user, order
                );
            console.log(res.data)
        
        }catch(err){
            console.error(err.message);
        }
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

                            <TableCell className={classes.thCell}>
                                Order ID
                                </TableCell>

                            <TableCell className={classes.thCell}>
                                Date Bought
                                </TableCell>

                            <TableCell className={classes.thCell}>
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

                                <TableCell>
                                    {row.orderID}
                                </TableCell>

                                <TableCell>
                                    {row.date}
                                </TableCell>

                                <TableCell>
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
        </>
    );
}