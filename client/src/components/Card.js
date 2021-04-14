import React from 'react';
import { Card } from 'react-bootstrap';
import ListGroup from 'react-bootstrap/ListGroup';

const productCard = ({ product }) => {

    return (
        <>
            <Card className='pt-3 my-3 rounded text-center shadow-lg bg-white rounded' style={{ border: 'none' }}>

                <Card.Body className={`${product.name} rounded text-black`}>

                        <Card.Title className="font-weight-bold" component="h1">
                            {product.name.charAt(0).toUpperCase() + product.name.slice(1)}
                        </Card.Title>

                        <ListGroup variant="flush">
                            <ListGroup.Item>Stock Quantity: {product.stock_quantity}</ListGroup.Item>
                            <ListGroup.Item>Monthly Restock Date: {product.monthly_restock_date}</ListGroup.Item>
                            <ListGroup.Item>Restock Quantity: {product.restock_quantity}</ListGroup.Item>
                        </ListGroup>

                </Card.Body>
                <div className="p-3 bg-color text-white text-left font-weight-bold">
                    Check Availability: 
                </div>
            </Card>
        </>
    )
}

export default productCard;