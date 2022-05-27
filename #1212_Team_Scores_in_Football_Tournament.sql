WITH h_ts AS (
    SELECT DISTINCT host_team AS team,
        SUM(CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals < guest_goals THEN 0
            ELSE 1
        END) OVER (PARTITION BY host_team) AS score_host
    FROM Matches
),
g_ts AS (
    SELECT DISTINCT guest_team AS team,
        SUM(CASE
            WHEN host_goals > guest_goals THEN 0
            WHEN host_goals < guest_goals THEN 3
            ELSE 1
        END) OVER (PARTITION BY guest_team) AS score_guest
    FROM Matches
)
SELECT 
    team_id, team_name, 
    (COALESCE (score_host, 0) + COALESCE (score_guest, 0)) AS num_points
FROM Teams
LEFT OUTER JOIN h_ts ON Teams.team_id = h_ts.team
LEFT OUTER JOIN g_ts ON Teams.team_id = g_ts.team
ORDER BY num_points DESC, team_id ASC;
