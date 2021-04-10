import React, {useState} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import axios from "axios"
import Container from '@material-ui/core/Container';

const styles = theme => ({
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
    width: '100%',
    marginTop: theme.spacing(1),
},
submit: {
    margin: theme.spacing(3, 0, 2),
},
});

class Login extends React.Component {
    constructor(props) {
        super();

        this.state = {
            name:"",
            password:""
        };

    this.changeName = this.changeName.bind(this)
    this.changePassword = this.changePassword.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
    }

    //changes email state to current value
    changeName(event) {
        this.setState({
            name: event.target.value
        })
    }

    //changes password to current value
    changePassword(event) {
        this.setState({
            password: event.target.value
        })
    }

    onSubmit(event){
        event.preventDefault()

        const signin = {
            name: this.state.name,
            password: this.state.password
        }

        axios.post("http://localhost:5000/login/", signin, {withCredentials:true})
        .then(response => { 
            this.setState({
            name:"",
            password:"",
            fireRedirect: true,
            })
        })
    }

    render(){
        return (
            <Container component="main" maxWidth="xs">
            <CssBaseline />
                <div className={classes.paper}>
                    <Avatar className={classes.avatar}>
                    <LockOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                    Sign in
                    </Typography>
                    <form className={classes.form} noValidate>


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
                        value = {this.state.name}
                        onChange={this.changeName}
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
                        value={this.state.password}
                        onChange={this.changePassword}
                    />


                    {/*Sign in button*/}
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                    >
                        Sign In
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
            </Container>
        )
    }
}


export default withStyles(styles, {withTheme: true})(Login);