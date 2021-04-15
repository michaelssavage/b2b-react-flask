import React, { useState} from 'react';
import { useHistory } from "react-router-dom";
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from "axios";

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

export default function Login() {

    const history = useHistory();

    async function handleLogin(){
        // event.preventDefault();

        try {
            history.push("/home");
        } catch (e){
            alert(e.message);
        }
    }

    const classes = useStyles();

    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    function handleSubmit(event){
        event.preventDefault()
        sendLogin()
    }

    const sendLogin = async () => {
        try{
            const res = await axios.post('http://localhost:5000/api/login', {
                withCredentials: true,
                name: name,
                password: password
            });

        // console.log(res.data);

        if (res.data === "Success"){
            // console.log(res);
            document.cookie = 'id='+name
            // return <Redirect to='/home'  /> 
            handleLogin();
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
                    <LockOutlinedIcon />
                </Avatar>

                <Typography component="h1" variant="h5">
                Login
                </Typography>
                <form className={classes.form} noValidate onSubmit={handleSubmit}>


                    {/*Username*/}
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


                    {/*Password*/}
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


                    {/*Sign in button*/}
                    <Button
                        fullWidth
                        type="submit"
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                    >
                        Login
                    </Button>



                    {/* link to sign up page */}  
                    <Grid container>
                        <Grid item>
                        <Link href="signup" variant="body2">                 
                            {"Don't have an account? Sign Up"}
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
    )
}