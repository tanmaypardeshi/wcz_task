import React, { useState } from 'react';
import { Button, CssBaseline, TextField, Grid, Typography, Container, FormControlLabel, Checkbox} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';


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
        marginTop: theme.spacing(3),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

const AddMatch = () => {
    const classes = useStyles();
    const [toggle, setToggle] = useState(false);
    const [home_team, setHomeTeam] = useState({
        'team_name': "",
        'fours': 0,
        'sixes': 0,
        'wickets': 0,
        "score": 0,
        "isFirstInnings": true
    });

    const [away_team, setAwayTeam] = useState({
        'team_name': "",
        'fours': 0,
        'sixes': 0,
        'wickets': 0,
        "score": 0,
        "isFirstInnings": true
    });

    const [data, setData] = useState({
        "winner": "",
        "man_of_the_match": "",
        "date": ""
    });

    const handleChange = (event) => {
        if(event.target.id === 'winner') {
            setData({...data, [event.target.id] : event.target.value});
        }
        if(event.target.id === 'date') {
            setData({...data, [event.target.id]: event.target.value});
        }
        if(event.target.id === 'man_of_the_match') {
            setData({...data, [event.target.id]: event.target.value});
        }
        if(event.target.id === 'home_team_name') {
            setHomeTeam({...home_team, 'team_name': event.target.value})
        }
        if(event.target.id === 'home_fours'){
            setHomeTeam({...home_team, 'fours': event.target.value})
        }
        if(event.target.id === 'home_sixes'){
            setHomeTeam({...home_team, 'sixes': event.target.value})
        }
        if(event.target.id === 'home_wickets'){
            setHomeTeam({...home_team, 'wickets': event.target.value})
        }
        if(event.target.id === 'home_score'){
            setHomeTeam({...home_team, 'score': event.target.value})
        }
        if(event.target.id === 'away_team_name') {
            setHomeTeam({...away_team, 'team_name': event.target.value})
        }
        if(event.target.id === 'away_fours'){
            setHomeTeam({...away_team, 'fours': event.target.value})
        }
        if(event.target.id === 'away_sixes'){
            setHomeTeam({...away_team, 'sixes': event.target.value})
        }
        if(event.target.id === 'away_wickets'){
            setHomeTeam({...away_team, 'wickets': event.target.value})
        }
        if(event.target.id === 'away_score'){
            setHomeTeam({...away_team, 'score': event.target.value})
        }
        if(event.target.id === 'isFirstInnings') {
            setToggle(!toggle);
            setHomeTeam({...home_team, 'isFirstInnings': !toggle})
            setAwayTeam({...away_team, 'isFirstInnings': toggle})
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(home_team);
        console.log(away_team);
        console.log(data);
    }

    return (
        <Container component="main" maxWidth="md">
        <CssBaseline />
            <div className={classes.paper}>
            
                <Typography variant="h1">
                Add a match
                </Typography>
                <br/>
                <form className={classes.form} noValidate onSubmit={handleSubmit}>
                    <Typography variant="h4" style={{paddingBottom:'2%'}}>
                        Enter General Match Details:
                    </Typography>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                        <TextField
                            autoComplete="winner"
                            name="winner"
                            variant="outlined"
                            required
                            fullWidth
                            id="winner"
                            label="Enter Winner Team Name"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={12}>
                        <TextField
                            autoComplete="date"
                            name="date"
                            variant="outlined"
                            required
                            fullWidth
                            id="date"
                            label="Enter Date of Match Played(Format: yyyy-mm-dd)"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={12}>
                        <TextField
                            autoComplete="man_of_the_match"
                            name="man_of_the_match"
                            variant="outlined"
                            required
                            fullWidth
                            id="man_of_the_match"
                            label="Enter Man of the Match"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                    </Grid>
                    <br/>
                    <Typography variant="h4" style={{paddingBottom:'2%'}}>
                        Enter Home Team Match Details:
                    </Typography>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                        <TextField
                            autoComplete="team_name"
                            name="team_name"
                            variant="outlined"
                            required
                            fullWidth
                            id="home_team_name"
                            label="Enter Home Team Name"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="fours"
                            name="home_fours"
                            variant="outlined"
                            required
                            fullWidth
                            id="home_fours"
                            label="Enter Fours"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="sixes"
                            name="home_sixes"
                            variant="outlined"
                            required
                            fullWidth
                            id="home_sixes"
                            label="Enter Sixes"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="wickets"
                            name="home_wickets"
                            variant="outlined"
                            required
                            fullWidth
                            id="home_wickets"
                            label="Enter wickets"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="score"
                            name="home_score"
                            variant="outlined"
                            required
                            fullWidth
                            id="home_score"
                            label="Enter score"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                    </Grid>
                    <Typography variant="h4" style={{paddingBottom:'2%'}}>
                        Enter Away Team Match Details:
                    </Typography>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                        <TextField
                            autoComplete="team_name"
                            name="away_team_name"
                            variant="outlined"
                            required
                            fullWidth
                            id="away_team_name"
                            label="Enter Away Team Name"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="fours"
                            name="away_fours"
                            variant="outlined"
                            required
                            fullWidth
                            id="away_fours"
                            label="Enter Fours"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="sixes"
                            name="away_sixes"
                            variant="outlined"
                            required
                            fullWidth
                            id="away_sixes"
                            label="Enter Sixes"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="wickets"
                            name="away_wickets"
                            variant="outlined"
                            required
                            fullWidth
                            id="away_wickets"
                            label="Enter wickets"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={3}>
                        <TextField
                            autoComplete="score"
                            name="away_score"
                            variant="outlined"
                            required
                            fullWidth
                            id="away_score"
                            label="Enter score"
                            onChange={handleChange}
                            autoFocus
                        />
                        </Grid>
                    </Grid>
                    <Grid item xs={12}>
                        <FormControlLabel
                            control={<Checkbox value={!toggle}  id="isFirstInnings" color="primary" />}
                            label="First Innings for Home Team?"
                            onChange={handleChange} 
                        />
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                    >
                        Add Match
                    </Button>
                </form>
            </div>
    </Container>
    )
}

export default AddMatch;