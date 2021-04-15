import React, { useState} from 'react';
import { useHistory } from "react-router-dom";
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import PersonAddIcon from '@material-ui/icons/PersonAdd';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from "axios"

import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}

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

export default function Signup() {

    const history = useHistory();

    async function handleSignUp(){
        // event.preventDefault();

        try {
            history.push("/login");
        } catch (e){
            alert(e.message);
        }
    }
    const classes = useStyles();

    const [name, setName] = useState("");
    const [password, setPassword] = useState("");

    function handleSubmit(event){
        event.preventDefault()
        // console.log( 'name:', name, 'Password: ', password); 
        sendSignUp()
    }

    const sendSignUp = async () => {
        try{
            const res = await axios.post('http://localhost:5000/api/signup', {
                withCredentials: true,
                name: name,
                password: password
            });

        // console.log(res.data);

        if (res.data === "Success"){
            handleMessage("Account Successfully Created", "success");
            setTimeout(() => {  
                handleSignUp(); 
            }, 1000);
            
        } else {
            handleMessage(res.data, "error");
        }

        }catch(err){
            console.error(err.message);
        }
    };

    const [open, setOpen] = useState(false);
    const [message, setMessage] = useState("");
    const [alertStyle, setAlertStyle] = useState("success");
    const handleMessage = (text, alert) => {
        setAlertStyle(alert);
        setMessage(text);
        setOpen(true);
    };

    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOpen(false);
    };

    return (
        <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>

            <Avatar className={classes.avatar}>
            <PersonAddIcon />
            </Avatar>

            <Typography component="h1" variant="h5">
            Sign Up
            </Typography>


            <form className={classes.form} noValidate onSubmit={handleSubmit}>
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="username"
                label="Username"
                name="username"
                autoComplete="username"
                autoFocus
                value= {name}
                onInput= {e => setName(e.target.value)}
            />


            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                value={password}
                onInput= {e => setPassword(e.target.value)}
            />


            <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
            >
                Sign Up
            </Button>
            <Grid container>

                <Grid item>
                <Link href="/login" variant="body2">                 {/* link to signin page */}  
                    {"Have an account? Login"}
                </Link>
                </Grid>
            </Grid>
            </form>
        </div>

        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>

            <Alert onClose={handleClose} severity={alertStyle}>
                {message}
            </Alert>
        </Snackbar>

        </Container>
    );
}