import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        boxShadow: "none",
        backgroundColor: "black" 
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    home: {
        flexGrow: 2
    },

    title: {
        flexGrow: 2
    },
}));

export default function Navbar() {
    const classes = useStyles();

    return (
        <div className={classes.root}>
        <AppBar position="static">
            <Toolbar>

                <Typography variant="h6" className={classes.home}>
                    <Link href="home" color="inherit">
                    Home
                    </Link>
                </Typography> 
                
                <Link href="orders" color="inherit">
                    <Button color="inherit">
                        My Orders
                    </Button>
                </Link>

                <Link href="login" color="inherit">
                    <Button color="inherit">
                        Sign out
                    </Button>
                </Link>

            </Toolbar>
        </AppBar>
        </div>
    );
}