import React, { useState, useEffect} from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import { Box } from '@material-ui/core'
import Button from '@material-ui/core/Button';

import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';

import { Row, Col } from 'react-bootstrap';

import Card from '../components/Card';
import Navbar from '../components/Navbar';
import axios from "axios";

import 'date-fns';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import { KeyboardDatePicker } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import moment from 'moment';

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
    root: {
        '& > *': {
            margin: theme.spacing(2),
            width: '25ch',
            },
    },
}));

const products = [
    {
        value: 'p1',
        label: 'Game Boy',
    },
    {
        value: 'p2',
        label: 'Apples',
    },
    {
        value: 'p3',
        label: 'Oranges',
    },
    {
        value: 'p4',
        label: 'Jolt cola',
    },
];

var dict = {
    "p1": "Game Boy",
    "p2": "Apples",
    "p3": "Oranges",
    "p4": "Jolt cola"
}

export default function Home() {
    const classes = useStyles();

    const [product, setProduct] = useState([]);
    const getProduct = async () => {

        try{
            const res = await axios.get('http://localhost:5000/api/products');
            // console.log(res.data)

            const productsArray = res.data;

            let productsArr = [];
            for(let i = 0; i < productsArray.length; i++){
                productsArr.push(productsArray[i]);
            }
            // console.log(productsArr)
            setProduct(productsArr);

        }catch(err){
            console.error(err.message);
        }
    };

    const [productOrder, setProductOrder] = useState('p1');
    const handleChange = (event) => {
        setProductOrder(event.target.value);
    };
    
    const [quantity, setQuantity] = useState("");
    const handleQuantity = (event) => {
        setQuantity(event.target.value);
    };

    // TODO chnage this todays date
    const [selectedDate, setSelectedDate] = useState(new Date('2021-05-13T21:11:54'));
    const handleDateChange = (date) => {
        setSelectedDate(date);
    };

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

    const PlaceNewOrder = async () => {

        try{
            const res = await axios.post('http://localhost:5000/api/order',
                {
                    customerID: "gerard",
                    product_name: dict[productOrder],
                    quantity: quantity,
                    day: moment(selectedDate, 'DD/MM/YYYY').format('DD'),
                    month: moment(selectedDate, 'DD/MM/YYYY').format('MM')
                }
            );

            if (res.data === "success"){
                handleMessage("Order Successful, sufficient stock!", "success");
                setQuantity("");
            } 
            else {
                handleMessage("Sorry, not enough stock to fulfil your order!", "warning");
            }
            
        }catch(err){
            console.error(err.message);
        }
    };

    useEffect(() => {
        getProduct();
    }, [])

    return (
        <>
            <Navbar />

            <Box display="flex" alignItems="center" justifyContent="center" className="mt-4">
                <form className={classes.root} noValidate autoComplete="off">

                    <TextField
                        id="standard-basic"
                        select
                        label="Select The Product"
                        value={productOrder}
                        onChange={handleChange}
                        >
                        {products.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                            {option.label}
                            </MenuItem>
                        ))}
                    </TextField>

                    <MuiPickersUtilsProvider utils={DateFnsUtils}>
                        <KeyboardDatePicker
                            disableToolbar
                            variant="inline"
                            format="dd/MM/yyyy"
                            margin="normal"
                            label="Choose The Order"
                            KeyboardButtonProps={{
                                'aria-label': 'change date',
                            }}
                            value={selectedDate} 
                            onChange={handleDateChange}
                        />
                    </MuiPickersUtilsProvider>

                    <TextField id="standard-basic" label="Select The Quantity" value={quantity} onChange={handleQuantity}/>

                    <Button variant="contained" color="secondary" size="large" onClick = {() => PlaceNewOrder()}>
                        Place Order
                    </Button>
                </form>
            </Box>

            <Container component="main" maxWidth="lg"> 
                <Row>
                    {product.map( p =>(

                        <Col key={p.name} xs={12} sm={12} md={6} lg={6} xl={6}>

                        <Card product={p}/>
                        </Col>
                    ))}
                </Row>
            </Container>

            <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>

                <Alert onClose={handleClose} severity={alertStyle}>
                    {message}
                </Alert>
            </Snackbar>
        </>
    );
}