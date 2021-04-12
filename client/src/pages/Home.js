import React, { useState, useEffect} from 'react';
import Navbar from '../components/Navbar';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Card from '../components/Card';
import { Row, Col } from 'react-bootstrap';
import axios from "axios";

const Home = () => {

    const [product, setProduct] = useState([]);

    const getProduct = async () => {
        let productArray = [];
        for(let i = 1; i <= 6; i ++){
            productArray.push(await getProductData(i));
        }
        
        setProduct(productArray);
    }

    const getProductData = async (id) => {
        const res = await axios.get(`https://pokeapi.co/api/v2/pokemon/${id}`); {/* this needs to be changed to the product apis */}
        return res;
    }

    useEffect(() => {
        getProduct();
    }, [])

    return (
        <>
            <Navbar />
            <Container component="main" maxWidth="s">  
                <Typography align="center" variant="h2"> 
                    Concurr B2B ordering service
                </Typography>


                <Row>
                    {product.map( p =>(

                        <Col key={p.data.name} xs={12} sm={12} md={4} lg={4} xl={4}>

                            <Card product={p.data}/>
                        </Col>
                    ))}
                </Row>


            </Container>
        </>
    );
}

export default Home;