import dash_html_components as html
import dash_daq as daq

height_ind = 18
width_ind = 18

habitsmonitor = html.Div([
    html.Div(["HABITS MONITOR"], style={"grid-column": "1/9"}),
    html.Div([""]),html.Div(["MON"]),html.Div(["TUE"]),html.Div(["WED"]),html.Div(["THU"]),html.Div(["FRI"]),html.Div(["SAT"]),html.Div(["SUN"]),
    html.Div([ "MIND"]),
                    html.Div([
                        daq.Indicator(
                            # color="green",
                            value=False,
                            width=width_ind,
                            height=height_ind
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind,
                            # style={"width": "100%", "height":"100%"}
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )

                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
    html.Div([
        "GYM"
    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
    html.Div([
        "CARDIO"
    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),

                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
                    html.Div([
                        daq.Indicator(
                            color="green",
                            value=True,
                            width=width_ind,
                            height=height_ind
                            ,
                        )
                    ]),
    html.Div([
        "GYM"
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),

    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),

    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),

    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        "CARDIO"
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),

    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
    html.Div([
        daq.Indicator(
            color="green",
            value=True,
            width=width_ind,
            height=height_ind
            ,
        )
    ]),
], className="habitsmonitor")