import React, {useState} from 'react';
import { Card } from 'react-bootstrap';
import ListGroup from 'react-bootstrap/ListGroup';

import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';

import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import axios from "axios";

const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
    },
    heading: {
        fontSize: theme.typography.pxToRem(15),
        fontWeight: theme.typography.fontWeightRegular,
    },
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120,
    },
    selectEmpty: {
        marginTop: theme.spacing(2),
    },
    projection: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center"
    }
}));

export default function ProductCard({ product }) {

    const classes = useStyles();
    const [date, setDate] = useState("");

    const handleChange = (event) => {
        setDate(event.target.value);
        // console.log(event.target.value);
        getProjection(event.target.value);
    };

    const [projection, setProjection] = useState(0);
    const getProjection = async (currentDate) => {
        try{

            // console.log(currentDate);
            const res = await axios.post("http://localhost:5000/api/availability_future", 
                {
                    product: product.productName,
                    date: currentDate
                }
            );

            console.log({
                    product: product.productName,
                    date: currentDate
                });

            console.log(res);

            setProjection(res.data);
        }catch(err){
            console.error(err.message);
        }
    };

    return (
        <>
            <Card className='pt-3 my-3 rounded text-center shadow-lg bg-white rounded' style={{ border: 'none' }}>

                <Card.Body className={`${product.productName} rounded text-black`}>

                        <Card.Title className="font-weight-bold" component="h1">
                            {product.productName.charAt(0).toUpperCase() + product.productName.slice(1)}
                        </Card.Title>

                        <ListGroup variant="flush">
                            <ListGroup.Item>Stock Quantity: {product.stock_quantity}</ListGroup.Item>
                            <ListGroup.Item>Monthly Restock Date: {product.monthly_restock_date}</ListGroup.Item>
                            <ListGroup.Item>Restock Quantity: {product.restock_quantity}</ListGroup.Item>
                        </ListGroup>

                </Card.Body>
                <div className="p-3 bg-color text-white text-left font-weight-bold">

                    <Accordion>
                        <AccordionSummary
                            expandIcon={<ExpandMoreIcon />}
                            aria-controls="panel1a-content"
                            id="panel1a-header"
                        >

                            <Typography className={classes.heading}>Check Stock Availability</Typography>

                        </AccordionSummary>
                        <AccordionDetails>

                            <FormControl variant="outlined" className={classes.formControl}>

                                <InputLabel id="demo-simple-select-outlined-label">Date</InputLabel>
                                <Select
                                    labelId="demo-simple-select-outlined-label"
                                    id="demo-simple-select-outlined"
                                    value={date}
                                    onChange={handleChange}
                                    label="Date"
                                >
                                    <MenuItem value="1">1 Month</MenuItem>
                                    <MenuItem value="3">3 Months</MenuItem>
                                    <MenuItem value="6">6 Months</MenuItem>
                                </Select>
                            </FormControl>

                            <Typography className={classes.projection}>
                                Projections for {product.productName}: {projection}
                            </Typography>
                        </AccordionDetails>

                    </Accordion>
                </div>
            </Card>
        </>
    );
}