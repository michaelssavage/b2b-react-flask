import React from 'react';
import Navbar from '../components/Navbar';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Card from '../components/Card';

export default function Home() {
    return (
        <>
            <Navbar />
            <Container component="main" maxWidth="s">  
                <Typography align="center" variant="h2"> 
                    Concurr B2B ordering service
                </Typography>

                <div>
            
                    <Row>
                        {pokemon.map( p =>(
                            <Col key={p.data.name} xs={12} sm={12} md={4} lg={4} xl={4}>
                                <Pokemon pokemon={p.data}/>
                            </Col>
                        ))}
                    </Row>
                </div>


            </Container>
        </>
    );
}
