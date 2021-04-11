import React from 'react';
import Navbar from '../components/Navbar';
import Typography from '@material-ui/core/Typography';

export default function Home() {
    return (
        <>
            <Navbar />
            <Typography align="center"> 
                <h1>Concurr B2B ordering service</h1>
            </Typography>
        </>
    );
}
