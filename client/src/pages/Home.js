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

        const res = await axios.get('http://localhost:5000/api/products');
        // console.log(res.data.products)

        const productsArray = res.data.products

        let productsArr = [];
        for(let i = 0; i < productsArray.length; i++){
            productsArr.push(productsArray[i])

        }
    
    // console.log(productsArr)
    setProduct(productsArr)
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