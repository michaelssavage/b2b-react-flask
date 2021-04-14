import React, { useState, useEffect} from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import { Box } from '@material-ui/core'
import Button from '@material-ui/core/Button';

import { Row, Col } from 'react-bootstrap';

import Card from '../components/Card';
import Navbar from '../components/Navbar';
import axios from "axios";

import 'date-fns';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import { KeyboardDatePicker } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import moment from 'moment';

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
        value: 'Game Boy',
        label: 'Game Boy',
    },
    {
        value: 'Apples',
        label: 'Apples',
    },
    {
        value: 'Oranges',
        label: 'Oranges',
    },
    {
        value: 'Jolt cola',
        label: 'Jolt cola',
    },
];

const Home = () => {

    const classes = useStyles();
    const [product, setProduct] = useState([]);

    const getProduct = async () => {

        try{
            const res = await axios.get('http://localhost:5000/api/products');
            // console.log(res.data.products)

            const productsArray = res.data.products;

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

    const [productOrder, setProductOrder] = useState('Game Boy');

    const handleChange = (event) => {
        setProductOrder(event.target.value);
    };
    
    const [quantity, setQuantity] = useState("");

    const handleQuantity = (event) => {
        setQuantity(event.target.value);
    };

    const [selectedDate, setSelectedDate] = useState(new Date('2021-05-13T21:11:54'));

    const handleDateChange = (date) => {
        setSelectedDate(date);
    };

    const PlaceNewOrder = async () => {

        try{
            await axios.post('http://localhost:5000/api/order',
                {
                    customerID: "gerard",
                    product_name: productOrder,
                    quantity: quantity,
                    day: moment(selectedDate, 'DD/MM/YYYY').format('DD'),
                    month: moment(selectedDate, 'DD/MM/YYYY').format('MM')
                }
            );
            console.log({
                product_name: productOrder,
                quantity: quantity,
                day: moment(selectedDate, 'DD/MM/YYYY').format('DD'),
                month: moment(selectedDate, 'DD/MM/YYYY').format('MM')
            })
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
            <Container component="main" maxWidth="xs" className="mt-5">  
                <Typography align="center" variant="h3"> 
                    Concurr B2B Order System
                </Typography>
            </Container>

            <Box display="flex" alignItems="center" justifyContent="center">
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
                            id="date-picker-inline"
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
        </>
    );
}

export default Home;