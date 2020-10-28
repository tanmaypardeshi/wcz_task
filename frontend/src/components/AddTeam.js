import React, { useEffect, useState } from 'react';
import { Button, CssBaseline, TextField, Grid, Typography, Container, Table, TableHead, TableRow, TableCell, Paper, TableBody, TableContainer} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
    paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    form: {
      width: '100%', // Fix IE 11 issue.
      marginTop: theme.spacing(3),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
}));

const AddTeam = () => {
    const classes = useStyles();
    const [data, setData] = useState({
        "team_name": "",
        "captain_name": "",
        "coach_name": ""
    });
    const [teams, setTeams] = useState([]);

    
    const handleChange = (event) => {
        setData({...data, [event.target.id]: event.target.value});
    }
    const handleSubmit = (event) => {
        event.preventDefault();
        axios({
            method: 'POST',
            headers : {
                "Content-Type": "application/json"
            },
            data : {
                "team_name": data.team_name,
                "coach_name": data.coach_name,
                "captain_name": data.captain_name
            },
            url: '/addteam/'
        })
        .then(response => {
            window.alert(response.status);
        })
        .catch(error => {
            window.alert(error);
        })
    }

    useEffect(() =>{
        axios({
            method:'GET',
            headers :{
                "Content-Type": "application/json"  
            },
            url:'/getteams',
        })
        .then(response => {
            setTeams(response.data.team_list);
        })
        .catch(error => {
            window.alert(error);
        })
    }, [teams])

    return (
        <Container component="main" maxWidth="md">
        <CssBaseline />
        <div className={classes.paper}>
          <Typography component="h1" variant="h5">
            Add a team
          </Typography>
          <form className={classes.form} noValidate onSubmit={handleSubmit}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  id="team_name"
                  label="Enter Team Name"
                  name="team_name"
                  onChange={handleChange}
                  autoComplete="team_name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  name="captain_name"
                  label="Enter Captain Name"
                  id="captain_name"
                  onChange={handleChange}
                  autoComplete="captain_name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  name="coach_name"
                  label="Enter Coach Name"
                  id="coach_name"
                  onChange={handleChange}
                  autoComplete="coach_name"
                />
              </Grid>
              
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Add Team
            </Button>
            </form>
        </div>
        <br/>
        <Typography variant="h3" align="center">
            All teams in the database
        </Typography>
        <TableContainer component={Paper} style={{
                marginTop: '2%',
            }}>
                <Table aria-label='simple_table'>
                    <TableHead style={{backgroundColor:'black'}}>
                        <TableRow>
                            <TableCell align="center">Team Number</TableCell>
                            <TableCell align="center">Team Name</TableCell>
                            <TableCell align="center">Captain Name</TableCell>
                            <TableCell align="center">Coach Name</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            teams.map((team, index) => {
                                return (
                                    <TableRow key={index}>
                                        <TableCell align="center">{index+1}</TableCell>
                                        <TableCell align="center">{team.team_name}</TableCell>
                                        <TableCell align="center">{team.captain_name}</TableCell>
                                        <TableCell align="center">{team.coach_name}</TableCell>
                                    </TableRow>
                                );
                            })
                        }
                    </TableBody>
                </Table>
            </TableContainer>
      </Container>
    )
}

export default AddTeam;