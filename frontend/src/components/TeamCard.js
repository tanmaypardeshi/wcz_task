import React from 'react';
import { Paper, Typography, Grid, makeStyles } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    paper: {

      padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.secondary,
    },
}));

const TeamCard = ({team_details}) => {
    const classes = useStyles();

    return(
        <>
        <Typography variant="h4" align="center">
            {team_details.team_name}
        </Typography>
        <br/>
        <Paper className={classes.paper}>
            <Typography variant="h5" align="center">
                <br/>
                Captain : {team_details.captain_name}<br/>
                Coach : {team_details.coach_name}<br/>
                Matches Played : {team_details.matches_played}<br/><br/>
                <Grid container spacing={3}>
                    <Grid item xs={6}>
                        Fours<br/>
                        {team_details.fours}
                    </Grid>
                    <Grid item xs={6}>
                        Sixes<br/>
                        {team_details.sixes}
                    </Grid>
                    <Grid item xs={6}>
                        Wickets Lost<br/>
                        {team_details.wickets}
                    </Grid>
                    <Grid item xs={6}>
                        Score<br/>
                        {team_details.score}
                    </Grid>
                </Grid>
            </Typography>
        </Paper>
        </>
    )
}

export default TeamCard;