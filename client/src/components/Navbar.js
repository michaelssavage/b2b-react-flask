import React from 'react';
import { useHistory } from "react-router-dom";
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

    button: {
        '&:hover': {
            color: '#e91e63',
        },
        textDecoration: 'none' 
    }
}));

export default function Navbar() {
    const classes = useStyles();

    const history = useHistory();
    async function handleSignOut(){
        document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        try {
            history.push("/login");
        } catch (e){
            alert(e.message);
        }
    }

    return (
        <div className={classes.root}>
        <AppBar position="static">
            <Toolbar>

                <Typography variant="h6" className={classes.home}>
                    <Link href="home" color="inherit" className={classes.button}>

                        <Button color="inherit">
                        Home
                        </Button>
                        
                    </Link>
                </Typography>
                
                <Link href="orders" color="inherit" className={classes.button}>
                    <Button color="inherit">
                        My Orders
                    </Button>
                </Link>

                <Link href="login" color="inherit" className={classes.button}>
                    <Button color="inherit" onClick={handleSignOut}>
                        Sign out
                    </Button>
                </Link>

            </Toolbar>

            <Typography variant="h4" align="center" className="mb-3">
                    Concurr B2B Order System
            </Typography> 

        </AppBar>
        </div>
    );
}