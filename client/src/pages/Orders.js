import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from "axios"
import Navbar from '../components/Navbar';

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
}));

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
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                    <div 
                        className={classes.paper}
                    >
                        {order}
                    </div>
            </Container>
        </>
    );
}