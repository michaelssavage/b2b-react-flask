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

function createData(name, date, quantity, restock, edit) {
    return { name, date, quantity, restock, edit };
}

const rows = [
    createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
    createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
    createData('Eclair', 262, 16.0, 24, 6.0),
    createData('Cupcake', 305, 3.7, 67, 4.3),
    createData('Gingerbread', 356, 16.0, 49, 3.9),
];

// const res = await axios.get('http://localhost:5000/api/products');
// const productsArray = res.data.products
// const rows = [];
{/*for (let i = 0; i < productsArray.length){

    if user == logged in user:
        rows.push(productsArray[i])
} */}

export default function Orders() {

    const classes = useStyles();

    const [order, setOrder] = useState("");

    const getOrder = async () => {
        try{
            const result = await axios.get('/check_orders')
            setOrder(result.data);
        
        }catch(err){
            console.error(err.message);
        }
    };

    useEffect(()=>{
        getOrder()},[])

    return (
        <>
            <Navbar />

            <Container component="main" maxWidth="xs" className="mt-5">  
                <Typography align="center" variant="h3"> 
                    My Orders
                </Typography>
            </Container>

            <Container component="main" maxWidth="s" className="mt-5">  
                <TableContainer component={Paper}>
                    <Table className={classes.table} aria-label="simple table">

                        <TableHead className= "table-color">
                        <TableRow>

                            <TableCell className={classes.thCell}>
                                Product Name
                            </TableCell>

                            <TableCell className={classes.thCell}>
                                Date Bought
                                </TableCell>

                            <TableCell className={classes.thCell}>
                                Quantity Bought
                                </TableCell>

                            <TableCell className={classes.thCell}>
                                Restock Date
                                </TableCell>

                            <TableCell align="right" className={classes.thCell}>
                                Edit Order
                                </TableCell>

                        </TableRow>
                        </TableHead>


                        <TableBody>
                        {rows.map((row) => (

                            <TableRow key={row.name}>

                                <TableCell component="th" scope="row">
                                    {row.name}
                                </TableCell>

                                <TableCell>
                                    {row.date}
                                </TableCell>

                                <TableCell>
                                    {row.quantity}
                                </TableCell>

                                <TableCell>
                                    {row.restock}
                                </TableCell>

                                <TableCell align="right">

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