import plotly.graph_objects as go

ARROW_SIZE = 2.5
ARROW_HEAD = 2
TEXT_SIZE = 32


def add_labels_to_ellipse(fig: go.Figure, a: float, b: float, c: float) -> go.Figure:
    """Adds geometric labels to an ellipse figure.

    Annotates the figure with dimension lines and markers for the
    centre, semi-major axis, semi-minor axis, foci, and focus offset.

    Args:
        fig: A Plotly figure containing an ellipse trace.
        a: Semi-major axis length.
        b: Semi-minor axis length.
        c: Distance from centre to focus (focal offset).

    Returns:
        The input figure with annotations added in-place.
    """
    fig = _label_centre(fig)
    fig = _label_semi_major(fig, a)
    fig = _label_semi_minor(fig, b)
    fig = _label_foci(fig, c)
    fig = _label_offset(fig, c)

    fig.update_layout(showlegend=False)
    return fig


def _label_centre(fig: go.Figure) -> go.Figure:
    _ = fig.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers",
            marker={"size": 5, "color": "black"},
        )
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[0],
            y=[-0.01],
            mode="text",
            text=["Centre"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _label_semi_major(fig: go.Figure, a: float) -> go.Figure:
    fig.add_annotation(
        x=0,
        y=0,
        ax=a,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    fig.add_annotation(
        x=a,
        y=0,
        ax=0,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[a / 2],
            y=[0],
            mode="text",
            text=["a"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _label_semi_minor(fig: go.Figure, b: float) -> go.Figure:
    fig.add_annotation(
        x=0,
        y=0,
        ax=0,
        ay=b,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    fig.add_annotation(
        x=0,
        y=b,
        ax=0,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[-0.01],
            y=[b / 2],
            mode="text",
            text=["b"],
            textposition="middle left",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _label_foci(fig: go.Figure, c: float) -> go.Figure:
    _ = fig.add_trace(
        go.Scatter(
            x=[-c],
            y=[0],
            mode="markers",
            marker={"size": 5, "color": "black"},
        )
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[c],
            y=[0],
            mode="markers",
            marker={"size": 5, "color": "black"},
        )
    )
    fig.add_annotation(
        x=c,
        y=0,
        ax=0,
        ay=-0.5,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    fig.add_annotation(
        x=-c,
        y=0,
        ax=0,
        ay=-0.5,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[0],
            y=[-0.5],
            mode="text",
            text=["Foci"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig


def _label_offset(fig: go.Figure, c: float) -> go.Figure:
    fig.add_annotation(
        x=0,
        y=0,
        ax=-c,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    fig.add_annotation(
        x=-c,
        y=0,
        ax=0,
        ay=0,
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=ARROW_HEAD,
        arrowsize=ARROW_SIZE,
    )
    _ = fig.add_trace(
        go.Scatter(
            x=[-(c / 2)],
            y=[0],
            mode="text",
            text=["c"],
            textposition="bottom center",
            textfont={"size": TEXT_SIZE},
        )
    )

    return fig
