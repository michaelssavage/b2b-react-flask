import React from 'react';
import { Card } from 'react-bootstrap';
import Button from 'react-bootstrap/Button'

const productCard = ({ product }) => {

    return (
        <>
            <Card className='my-3 p-3 rounded text-center shadow p-3 mb-5 bg-white rounded' style={{ border: 'none' }}>


                <Card.Body className={`${product.types[0].type.name} rounded text-black`}>

                        <Card.Title as='div'>
                            #{product.id}: {product.name.charAt(0).toUpperCase() + product.name.slice(1)}
                        </Card.Title>

                        <Card.Text> 
                            {/*
                            product.stock_quantity
                            product.monthly_restock_date
                            product.restock_quantity
                            */}
                            Some quick example text to build on the card title and make up the bulk of
                            the card's content.
                        </Card.Text>

                </Card.Body>
                <div className="pt-2">
                    <Button variant="info">Find Out More!</Button> 
                </div>
            </Card>
        </>
    )
}

export default productCard;