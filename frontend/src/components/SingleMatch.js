import { Container, Paper, Typography, Grid } from '@material-ui/core';
import React, {useState, useEffect} from 'react';
import { useLocation } from 'react-router-dom';
import TeamCard from './TeamCard';
import axios from 'axios';

const SingleMatch = () => {
    const location = useLocation();
    const [id, setID] = useState(1);
    const [data, setData] = useState({
        match_id: 0,
        winner: "",
        man_of_the_match: "",
        date: ""
    });
    const [team1, setTeam1] = useState({
        team_id: 0,
        team_name: "",
        coach_name: "",
        captain_name: "",
        matches_played: 0,
        fours: 0,
        sixes: 0,
        wickets: 0,
        score: 0
    });
    const [team2, setTeam2] = useState({
        team_id: 0,
        team_name: "",
        coach_name: "",
        captain_name: "",
        matches_played: 0,
        fours: 0,
        sixes: 0,
        wickets: 0,
        score: 0
    });

    useEffect(() => {
        let path = location.pathname;
        path = parseInt(path.charAt(path.length - 1));
        setID(path);
        axios({
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            },
            url: `/getmatch/${id}/`
        })
        .then(response => {
            setData(response.data);
            setTeam1(response.data.team1);
            setTeam2(response.data.team2);
        })
        .catch(error => {
            window.alert(error);
        })
	}, [location, id])
    
    return (
        <Container>
            <Typography variant="h2" align="center" style={{marginTop:'4%'}}>
                Details of Match {id}
            </Typography>
            <Paper elevation={3} style={{
                marginTop: '2%'
            }}>
                <Typography variant="h5" style={{padding:'2%'}}>
                    Match ID: {data.match_id}<br/>
                    Winner: {data.winner}<br/>
                    Man of the match: {data.man_of_the_match}<br/>
                    Date Played: {data.date}<br/>
                </Typography>
            </Paper>
            <Grid container spacing={3} style={{marginTop:'5%'}}>
                <Grid item xs={4}>
                    <TeamCard team_details={team1}/>
                </Grid>
                <Grid item xs={3}>
                    <Typography variant="h2" align="center" style={{
                        marginTop:'55%'
                    }}>
                        V/S
                    </Typography>
                </Grid>
                <Grid item xs={4}>
                    <TeamCard team_details={team2}/>
                </Grid>
            </Grid>
        </Container>
    )
}

export default SingleMatch;