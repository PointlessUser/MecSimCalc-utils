from typing import Union, Tuple, Optional, Dict, Any
import matplotlib.pyplot as plt
import numpy as np
import math


def draw_arrow(
    start: Union[tuple, list],
    end: Union[tuple, list],
    thickness: int = 5,
    color: str = "black",
    text: Optional[str] = None,
    text_offset: float = 0.1,
    head_width: float = 0.08,
    head_length: float = 0.08,
    fontsize: int = 12,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_arrow(
        start: Union[tuple, list],
        end: Union[tuple, list],
        thickness: int = 5,
        color: str = "black",
        text: Optional[str] = None,
        text_offset: float = 0.1,
        head_width: float = 0.08,
        head_length: float = 0.08,
        fontsize: int = 12,
        ax: Optional[plt.Axes] = None,
    ) -> None

    Draws an arrow between two points on a plot with optional text annotation.

    Parameters
    ----------
    start : Union[tuple, list]
        The starting point of the arrow (x, y).
    end : Union[tuple, list]
        The ending point of the arrow (x, y).
    thickness : int, optional
        The thickness of the arrow line. (Default is 5)
    color : str, optional
        The color of the arrow. (Default is 'black')
    text : Optional[str], optional
        Text to display near the arrow. (Default is None)
    text_offset : float, optional
        Distance from the arrow end point where the text will be placed. (Default is 0.1)
    head_width : float, optional
        Width of the arrow head. (Default is 0.08)
    head_length : float, optional
        Length of the arrow head. (Default is 0.08)
    fontsize : int, optional
        Font size of the text. (Default is 12)
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes. (Default is None)


    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> pltdraw.draw_arrow((0, 0), (1, 1), thickness=2, color='red', text='Arrow', text_offset=0.1, head_width=0.1, head_length=0.1, fontsize=10)
    >>> plt.xlim(-1, 2)
    >>> plt.ylim(-1, 2)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    start, end = np.array(start), np.array(end)
    ax.arrow(
        start[0],
        start[1],
        end[0] - start[0],
        end[1] - start[1],
        head_width=head_width,
        head_length=head_length,
        linewidth=thickness,
        color=color,
        length_includes_head=True,
    )
    if text:
        arrow_vector = end - start
        text_position = end + text_offset * arrow_vector / np.linalg.norm(arrow_vector)
        ax.text(text_position[0], text_position[1], text, fontsize=fontsize)


def calculate_midpoint(
    coord1: Tuple[float, float], coord2: Tuple[float, float]
) -> Tuple[float, float]:
    """
    >>> calculate_midpoint(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> Tuple[float, float]

    Calculates the midpoint between two coordinates.

    Parameters
    ----------
    coord1 : Tuple[float, float]
        The first coordinate (x, y).
    coord2 : Tuple[float, float]
        The second coordinate (x, y).

    Returns
    -------
    * `Tuple[float, float]`
        The midpoint (x, y).

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> midpoint = pltdraw.calculate_midpoint((0, 0), (2, 2))
    >>> print(midpoint)
    (1.0, 1.0)
    """
    x1, y1 = coord1
    x2, y2 = coord2
    return (x1 + x2) / 2, (y1 + y2) / 2


def draw_arc(
    radius: float,
    start_angle: float,
    end_angle: float,
    center: tuple = (0, 0),
    color: str = "red",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_arc(
        radius: float,
        start_angle: float,
        end_angle: float,
        center: tuple = (0, 0),
        color: str = "red",
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws an arc of a circle with a given radius between two angles.

    Parameters
    ----------
    radius : float
        The radius of the arc.
    start_angle : float
        The starting angle of the arc in radians.
    end_angle : float
        The ending angle of the arc in radians.
    center : tuple, optional
        The center of the arc (Default is (0, 0)).
    color : str, optional
        The color of the arc (Default is 'red').
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).


    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> pltdraw.draw_arc(5, 0, np.pi/2)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if abs(end_angle - start_angle) > 2 * np.pi:
        end_angle = 2 * np.pi
        start_angle = 0

    angles = np.linspace(start_angle, end_angle, 200)
    x = radius * np.cos(angles) + center[0]
    y = radius * np.sin(angles) + center[1]
    ax.plot(x, y, color=color)
    ax.axis("equal")


def create_blank_canvas(
    width: int = 1000, height: int = 1000, color: str = "white"
) -> plt.Axes:
    """
    >>> create_blank_canvas(width: int = 1000, height: int = 1000, color: str = "white") -> plt.Axes

    Creates a blank canvas with specified width, height, and background color.

    Parameters
    ----------
    width : int, optional
        The width of the canvas in pixels (Default is 1000).
    height : int, optional
        The height of the canvas in pixels (Default is 1000).
    color : str, optional
        The background color of the canvas (Default is 'white').

    Returns
    -------
    * `plt.Axes`
        The Axes object of the created blank canvas.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.create_blank_canvas(800, 600, color='lightgrey')
    >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))
    ax.set_facecolor(color)
    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False,
    )
    ax.grid(True, alpha=0.5)
    ax.minorticks_on()
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="gray")
    return ax


def draw_three_axes(
    arrow_length: float = 1.0,
    arrow_thickness: float = 2.0,
    text_offset: float = 0.1,
    longx: float = 1.5,
    axis_y_negative: bool = False,
    axis_x_negative: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_three_axes(
        arrow_length: float = 1.0,
        arrow_thickness: float = 2.0,
        text_offset: float = 0.1,
        longx: float = 1.5,
        axis_y_negative: bool = False,
        axis_x_negative: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws a set of three axes (x, y, z) with optional negative directions for x and y.

    Parameters
    ----------
    arrow_length : float, optional
        The length of the arrows representing the axes (Default is 1.0).
    arrow_thickness : float, optional
        The thickness of the arrows (Default is 2.0).
    text_offset : float, optional
        The distance between the end of the arrow and the label text (Default is 0.1).
    longx : float, optional
        The factor to adjust the length of the diagonal x-axis (Default is 1.5).
    axis_y_negative : bool, optional
        Whether to draw the negative y-axis (Default is False).
    axis_x_negative : bool, optional
        Whether to draw the negative x-axis (Default is False).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `plt.Axes`
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.draw_three_axes(arrow_length=1, arrow_thickness=2, text_offset=0.1, longx=1.5, axis_y_negative=True, axis_x_negative=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(0, arrow_length + text_offset, "z", fontsize=12, ha="center", va="bottom")

    ax.arrow(
        0,
        0,
        arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(arrow_length + text_offset, 0, "y", fontsize=12, ha="left", va="center")

    if axis_y_negative:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.arrow(
        0,
        0,
        -arrow_length / longx,
        -arrow_length / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(
        -arrow_length / longx - text_offset / 1.5,
        -arrow_length / longx - text_offset / 1.5,
        "x",
        fontsize=12,
        ha="right",
        va="top",
    )

    if axis_x_negative:
        ax.arrow(
            0,
            0,
            arrow_length / longx,
            arrow_length / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.axis("equal")
    return ax


def draw_two_inclined_axes(
    arrow_length: float = 1.0,
    arrow_thickness: float = 2.0,
    text_offset: float = 0.1,
    longx: float = 1.5,
    draw_negative_y: bool = False,
    draw_negative_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_two_inclined_axes(
        arrow_length: float = 1.0,
        arrow_thickness: float = 2.0,
        text_offset: float = 0.1,
        longx: float = 1.5,
        draw_negative_y: bool = False,
        draw_negative_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws two inclined axes (x and y) with optional negative directions.

    Parameters
    ----------
    arrow_length : float, optional
        The length of the arrows representing the axes (Default is 1.0).
    arrow_thickness : float, optional
        The thickness of the arrows (Default is 2.0).
    text_offset : float, optional
        The distance between the end of the arrow and the label text (Default is 0.1).
    longx : float, optional
        The factor to adjust the length of the diagonal y-axis (Default is 1.5).
    draw_negative_y : bool, optional
        Whether to draw the negative y-axis (Default is False).
    draw_negative_x : bool, optional
        Whether to draw the negative x-axis (Default is False).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `plt.Axes`
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.draw_two_inclined_axes(arrow_length=1, arrow_thickness=2, text_offset=0.1, longx=1.5, draw_negative_y=True, draw_negative_x=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    ax.arrow(
        0,
        0,
        arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(arrow_length + text_offset, 0, "x", fontsize=12, ha="left", va="center")

    if draw_negative_x:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.arrow(
        0,
        0,
        arrow_length / longx,
        arrow_length / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(
        arrow_length / longx + text_offset / 1.5,
        arrow_length / longx + text_offset / 1.5,
        "y",
        fontsize=12,
        ha="left",
        va="bottom",
    )

    if draw_negative_y:
        ax.arrow(
            0,
            0,
            -arrow_length / longx,
            -arrow_length / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.axis("equal")
    return ax


def plot_line_segment(
    start: Tuple[float, float],
    end: Tuple[float, float],
    line_properties: Dict[str, Any] = None,
    label: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_properties: Dict[str, Any] = None,
    alpha: float = 0.8,
    ax: Optional[plt.Axes] = None,
) -> Tuple[float, float]:
    """
    >>> def plot_line_segment(
        start: Tuple[float, float],
        end: Tuple[float, float],
        line_properties: Dict[str, Any] = None,
        label: str = "",
        min_spacing: float = 150,
        fontsize: int = 15,
        text_properties: Dict[str, Any] = None,
        alpha: float = 0.8,
        ax: Optional[plt.Axes] = None,
    ) -> Tuple[float, float]:

    Plots a line segment between two points and adds a label at the end point.

    Parameters
    ----------
    start : Tuple[float, float]
        The starting point of the line segment (x, y).
    end : Tuple[float, float]
        The ending point of the line segment (x, y).
    line_properties : Dict[str, Any], optional
        Properties for the line, including color, linewidth, and linestyle.
        Default is {'color': 'k', 'linewidth': 1, 'linestyle': 'dashed'}.
    label : str, optional
        The text to display near the end point of the line segment. Default is "".
    min_spacing : float, optional
        Minimum spacing for the text from the end point. Default is 150.
    fontsize : int, optional
        Font size of the text. Default is 15.
    text_properties : Dict[str, Any], optional
        Dictionary specifying properties for the text, such as horizontal and vertical alignment.
        Default is {'ha': 'center', 'va': 'bottom'}.
    alpha : float, optional
        Transparency level of the line segment. Default is 0.8.
    ax : plt.Axes, optional
        The Axes object to plot on. If None, the current axes will be used.

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecismcalc.plot_draw as pltdraw
    >>> start = (100, 200)
    >>> end = (400, 500)
    >>> pltdraw.plot_line_segment(start, end, label="Segment", min_spacing=50)
    (400, 500)
    >>> plt.show()
    """
    if line_properties is None:
        line_properties = {"color": "k", "linewidth": 1, "linestyle": "dashed"}
    if text_properties is None:
        text_properties = {"ha": "center", "va": "bottom"}

    ax = ax or plt.gca()

    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        **line_properties,
        alpha=alpha,
    )

    # Calculate spacing for text
    distance = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    space = max(0.1 * distance, min_spacing)

    # Calculate the angle of the line
    angle = np.arctan2(end[1] - start[1], end[0] - start[0])

    # Calculate text position with an offset to avoid overlap
    x_text = end[0] + space * np.cos(angle - np.pi / 4)
    y_text = end[1] + space * np.sin(angle - np.pi / 4)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Adjust text position if it is outside the plot
    x_text = np.clip(x_text, xlim[0], xlim[1])
    y_text = np.clip(y_text, ylim[0], ylim[1])

    ax.text(
        x_text,
        y_text,
        label,
        fontsize=fontsize,
        color="k",
        **text_properties,
    )

    return end


def plot_annotate_arrow(
    start: tuple,
    angle: float,
    length: float,
    degrees: bool = False,
    text: str = "",
    text_offset: float = 0.1,
    fontsize: int = 11,
    text_align: dict = None,
    arrow_props: dict = None,
    reverse: bool = False,
    center_text: bool = False,
    reverse_text: bool = False,
    alpha: float = 0.8,
    ax: Optional[plt.Axes] = None,
) -> tuple:
    """
    >>> plot_annotate_arrow(
        start: tuple,
        angle: float,
        length: float,
        degrees: bool = False,
        text: str = "",
        text_offset: float = 0.1,
        fontsize: int = 11,
        text_align: dict = None,
        arrow_props: dict = None,
        reverse: bool = False,
        center_text: bool = False,
        reverse_text: bool = False,
        alpha: float = 0.8,
        ax: Optional[plt.Axes] = None
    ) -> tuple:

    Plots an annotated arrow starting from a given point and extending in a given direction.

    Parameters
    ----------
    start : tuple
        The starting point of the arrow (x, y).
    angle : float
        The angle of the arrow in degrees or radians.
    length : float
        The length of the arrow.
    degrees : bool, optional
        Whether the angle is given in degrees. Default is `False`.
    text : str, optional
        The text to display near the arrow.
    text_offset : float, optional
        Distance from the arrow end point where the text will be placed. Default is `0.1`.
    fontsize : int, optional
        Font size of the text Default is `11`.
    text_align : dict, optional
        Dictionary specifying horizontal and vertical alignment of the text. Default is `{'ha': 'center', 'va': 'top'}`.
    arrow_props : dict, optional
        Properties for the arrow, including width, head_width, head_length, fill color (fc), and edge color (ec). Default is `{'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'}`.
    reverse : bool, optional
        Whether to reverse the direction of the arrow. Default is `False`.
    center_text : bool, optional
        Whether to place the text in the center of the arrow. Default is `False`.
    reverse_text : bool, optional
        Whether to reverse the text orientation. Default is `False`.
    alpha : float, optional
        Transparency level of the arrow. Default is `0.8`.
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes. Default is `None`.

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the arrow (x, y).

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> start = (100, 200)
    >>> angle = 45
    >>> length = 100
    >>> pltdraw.plot_annotate_arrow(start, angle, length, text="Arrow", text_offset=50, degrees=True)
    (170.71067811865476, 270.71067811865476)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    arrow_props = arrow_props or {
        "width": 2,
        "head_width": 15,
        "head_length": 15,
        "fc": "black",
        "ec": "black",
    }
    text_align = text_align or {"ha": "center", "va": "top"}

    end = (
        start[0] + (length - arrow_props["head_length"]) * np.cos(angle),
        start[1] + (length - arrow_props["head_length"]) * np.sin(angle),
    )
    if not reverse:
        ax.arrow(
            *start,
            *(end[0] - start[0], end[1] - start[1]),
            **arrow_props,
            alpha=alpha,
        )
    else:
        end = (
            start[0] + length * np.cos(angle),
            start[1] + length * np.sin(angle),
        )
        start = (
            start[0] + 0 * np.cos(angle),
            start[1] + 0 * np.sin(angle),
        )
        ax.arrow(
            *end,
            *(start[0] - end[0], start[1] - end[1]),
            **arrow_props,
            alpha=alpha,
        )

    mid = (
        start[0] + 0.5 * length * np.cos(angle),
        start[1] + 0.5 * length * np.sin(angle),
    )
    if not center_text:
        space = max(0.1 * length, text_offset)
        text_x = end[0] + space * np.cos(angle)
        text_y = end[1] + space * np.sin(angle)
    else:
        rot_angle = -angle if angle < np.pi / 2 else (np.pi - angle)
        rot_angle = rot_angle + np.pi if reverse_text else rot_angle
        text_x = mid[0] + text_offset * np.cos(np.pi / 2 + angle)
        text_y = mid[1] + text_offset * np.sin(np.pi / 2 + angle)

    # Adjust text position to be within plot boundaries
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    text_x = max(min(text_x, xlim[1]), xlim[0])
    text_y = max(min(text_y, ylim[1]), ylim[0])

    ax.text(
        text_x,
        text_y,
        text,
        fontsize=fontsize,
        color="k",
        **text_align,
    )

    end = (
        start[0] + length * np.cos(angle),
        start[1] + length * np.sin(angle),
    )

    return tuple(map(float, end))


def draw_custom_arrow(
    start: Tuple[float, float],
    end: Tuple[float, float],
    factor: float = 0.5,
    max_value: float = 100,
    arrow_vector_length: float = 50,
    arrow_width: float = 5,
    arrow_color: str = "blue",
    line_width: float = 1,
    text: str = "",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    Draws a custom arrow from a start point to an end point on a given axis.

    Parameters
    ----------
    start : Tuple[float, float], optional
        The starting point of the arrow (x, y).
    end : Tuple[float, float], optional
        The end point of the arrow (x, y).
    factor : float, optional
        Factor to adjust the position of the text relative to the arrow. Default is 0.5.
    max_value : float, optional
        Maximum value for scaling the arrow length. Default is 100
    arrow_vector_length : float, optional
        Length of the arrow vector. Default is 50.
    arrow_width : float, optional
        Width of the arrow head. Default is 5.
    arrow_color : str, optional
        Color of the arrow. Default is 'blue'.
    line_width : float, optional
        Width of the arrow line. Default is `1`.
    text : str, optional
        Text to display near the end of the arrow. default is "".
    ax : matplotlib.axes.Axes, optional
        The Axes object to draw the arrow on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecismcalc.plot_draw as pltdraw
    >>> pltdraw.draw_custom_arrow((0, 0), (100, 100), text='arrow')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    start = np.array(start)
    end = np.array(end)
    arrow_vector = end - start
    arrow_direction = arrow_vector * (arrow_vector_length / (max_value * 2))
    arrow_end = start + arrow_direction
    text_offset = arrow_direction * factor

    ax.arrow(
        start[0],
        start[1],
        arrow_direction[0],
        arrow_direction[1],
        head_width=arrow_width,
        head_length=arrow_width * 2,
        fc=arrow_color,
        ec=arrow_color,
        lw=line_width,
    )

    if text:
        text_x = arrow_end[0] + text_offset[0]
        text_y = arrow_end[1] + text_offset[1]

        text_x = np.clip(text_x, *ax.get_xlim())
        text_y = np.clip(text_y, *ax.get_ylim())

        ax.text(text_x, text_y, f"${text}$", fontsize=12, ha="center", va="top")


def calculate_arrow_endpoint_pixels(
    start: tuple, angle: float, length: float, degrees: bool = False
) -> tuple:
    """
    >>> def calculate_arrow_endpoint_pixels(
        start: tuple, angle: float, length: float, degrees: bool = False
    ) -> tuple:

    Calculates the end point of an arrow in pixel coordinates.

    Parameters
    ----------
    start : tuple
        The starting point of the arrow (x, y) in pixel coordinates.
    angle : float
        The angle of the arrow in degrees or radians.
    length : float
        The length of the arrow.
    degrees : bool, optional
        Whether the angle is given in degrees (Default is False).

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the arrow (x, y) in pixel coordinates.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_arrow_endpoint_pixels((100, 200), 45, 50, degrees=True)
    (135.35533905932738, 235.35533905932738)
    """
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    end_x = float(start[0] + length * np.cos(angle))
    end_y = float(start[1] + length * np.sin(angle))

    return end_x, end_y


def plot_segment(
    start: Tuple[float, float],
    angle: float,
    length: float,
    degrees: bool = False,
    line_props: dict = None,
    text: str = "",
    text_offset: float = 0.1,
    fontsize: int = 15,
    text_align: dict = None,
    alpha: float = 0.8,
    ax: Optional[plt.Axes] = None,
) -> tuple:
    """
    >>> def plot_segment(
        start: tuple,
        angle: float,
        length: float,
        degrees: bool = False,
        line_props: dict = None,
        text: str = "",
        text_offset: float = 0.1,
        fontsize: int = 15,
        text_align: dict = None,
        alpha: float = 0.8,
        ax: Optional[plt.Axes] = None,
    ) -> Tuple[float, float]:

    Plots a line segment starting from a given point with a specific angle and length.

    Parameters
    ----------
    start : tuple
        The starting point of the line segment (x, y).
    angle : float
        The angle of the line segment in degrees or radians.
    length : float
        The length of the line segment.
    degrees : bool, optional
        Whether the angle is given in degrees (Default is False).
    line_props : dict, optional
        Properties of the line segment such as color and linewidth (Default is {'color': 'blue', 'linewidth': 1}).
    text : str, optional
        The text to display near the end of the line segment.
    text_offset : float, optional
        Minimum spacing between the end of the line segment and the text (Default is 0.1).
    fontsize : int, optional
        The font size of the text (Default is 15).
    text_align : dict, optional
        Location parameters for the text (Default is {'ha': 'center', 'va': 'top'}).
    alpha : float, optional
        The alpha value for transparency (Default is 0.8).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_segment((100, 200), 45, 50, text='Value', degrees=True)
    (135.35533905932738, 235.35533905932738)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    end = (
        start[0] + length * np.cos(angle),
        start[1] + length * np.sin(angle),
    )

    line_props = line_props or {"color": "blue", "linewidth": 1}
    text_align = text_align or {"ha": "center", "va": "top"}

    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        **line_props,
        alpha=alpha,
    )

    mid = (
        start[0] + 0.5 * length * np.cos(angle),
        start[1] + 0.5 * length * np.sin(angle),
    )
    offset = max(0.1 * length, text_offset)
    ax.text(
        end[0] + offset * np.cos(angle),
        end[1] + offset * np.sin(angle),
        text,
        fontsize=fontsize,
        color="k",
        **text_align,
    )

    return end


def plot_segment_dashed(
    start: tuple,
    angle: float,
    length: float,
    degrees: bool = False,
    line_props: dict = None,
    text: str = "",
    text_offset: float = 0.1,
    fontsize: int = 15,
    text_align: dict = None,
    alpha: float = 0.8,
    ax: Optional[plt.Axes] = None,
) -> Tuple[float, float]:
    """
    >>> def plot_segment_dashed(
        start: Tuple[float, float],
        angle: float,
        length: float,
        degrees: bool = False,
        line_props: dict = None,
        text: str = "",
        text_offset: float = 0.1,
        fontsize: int = 15,
        text_align: dict = None,
        alpha: float = 0.8,
        ax: Optional[plt.Axes] = None,
    ) -> Tuple[float, float]:

    Plots a dashed line segment starting from a given point with a specific angle and length.

    Parameters
    ----------
    start : Tuple[float, float]
        The starting point of the line segment (x, y).
    angle : float
        The angle of the line segment in degrees or radians.
    length : float
        The length of the line segment.
    degrees : bool, optional
        Whether the angle is given in degrees (Default is False).
    line_props : dict, optional
        Properties of the line segment such as color and linewidth (Default is {'color': 'blue', 'linestyle': 'dashed', 'linewidth': 1}).
    text : str, optional
        The text to display near the end of the line segment.
    text_offset : float, optional
        Minimum spacing between the end of the line segment and the text (Default is 0.1).
    fontsize : int, optional
        The font size of the text (Default is 15).
    text_align : dict, optional
        Location parameters for the text (Default is {'ha': 'center', 'va': 'top'}).
    alpha : float, optional
        The alpha value for transparency (Default is 0.8).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_segment_dashed((100, 200), 45, 50, text='Value', degrees=True)
    (135.35533905932738, 235.35533905932738)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    end = (
        start[0] + length * np.cos(angle),
        start[1] + length * np.sin(angle),
    )

    line_props = line_props or {"color": "blue", "linestyle": "dashed", "linewidth": 1}
    text_align = text_align or {"ha": "center", "va": "top"}

    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        **line_props,
        alpha=alpha,
    )

    mid = (
        start[0] + 0.5 * length * np.cos(angle),
        start[1] + 0.5 * length * np.sin(angle),
    )
    if text:
        offset = max(0.1 * length, text_offset)
        ax.text(
            end[0] + offset * np.cos(angle),
            end[1] + offset * np.sin(angle),
            text,
            fontsize=fontsize,
            color="k",
            **text_align,
        )

    return end


def draw_custom_circle(
    center: Tuple[float, float] = (0, 0),
    radius: float = 10,
    color: str = "black",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_custom_circle(
        center: Tuple[float, float] = (0, 0),
        radius: float = 10,
        color: str = "black",
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws a custom circle on a given axis.

    Parameters
    ----------
    center : Tuple[float, float], optional
        The center point of the circle (x, y). Default is (0, 0).
    radius : float, optional
        The radius of the circle. (Default is 10)
    color : str, optional
        The color of the circle. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the circle on. If None, creates a new figure and axis.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_custom_circle((100, 100), radius=20, color='red')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    # Calculate the area in points^2 for the scatter size parameter
    area = np.pi * (radius**2)

    ax.scatter(center[0], center[1], s=area, color=color)


def draw_rounded_rectangle(
    width: float,
    height: float,
    center: Tuple[float, float] = (0, 0),
    corner_radius: float = 0.5,
    color: str = "black",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def draw_rounded_rectangle(
        width: float,
        height: float,
        center: Tuple[float, float] = (0, 0),
        corner_radius: float = 0.5,
        color: str = "black",
        ax: Optional[plt.Axes] = None,
    ) -> None:

    Draws a rounded rectangle with specified properties.

    Parameters
    ----------
    width : float
        The width of the rounded rectangle.
    height : float
        The height of the rounded rectangle.
    center : Tuple[float, float], optional
        The center point of the rectangle (x, y). Default is (0, 0).
    corner_radius : float, optional
        The radius of the corners. Default is 0.5.
    color : str, optional
        The color of the rectangle. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the rectangle on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_rounded_rectangle(4, 2, center = (0,0), corner_radius = 0.5,  color='blue')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    x_center, y_center = center
    x1 = x_center - width / 2
    y1 = y_center - height / 2
    x2 = x_center + width / 2
    y2 = y_center + height / 2

    # Draw the straight edges
    plt.plot([x1 + corner_radius, x2 - corner_radius], [y1, y1], color=color)
    plt.plot([x2, x2], [y1 + corner_radius, y2 - corner_radius], color=color)
    plt.plot([x2 - corner_radius, x1 + corner_radius], [y2, y2], color=color)
    plt.plot([x1, x1], [y2 - corner_radius, y1 + corner_radius], color=color)

    # Draw the corners
    corner_angles = np.linspace(np.pi, 1.5 * np.pi, 50)
    plt.plot(
        x1 + corner_radius + corner_radius * np.cos(corner_angles),
        y1 + corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # bottom-left corner

    corner_angles = np.linspace(1.5 * np.pi, 2 * np.pi, 50)
    plt.plot(
        x2 - corner_radius + corner_radius * np.cos(corner_angles),
        y1 + corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # bottom-right corner

    corner_angles = np.linspace(0, 0.5 * np.pi, 50)
    plt.plot(
        x2 - corner_radius + corner_radius * np.cos(corner_angles),
        y2 - corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # top-right corner

    corner_angles = np.linspace(0.5 * np.pi, np.pi, 50)
    plt.plot(
        x1 + corner_radius + corner_radius * np.cos(corner_angles),
        y2 - corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # top-left corner


def calculate_intersection_point(
    point1: Tuple[float, float],
    angle1: float,
    point2: Tuple[float, float],
    angle2: float,
    degrees: bool = False,
) -> Tuple[float, float]:
    """
    >>> def calculate_intersection_point(
        point1: Tuple[float, float],
        angle1: float,
        point2: Tuple[float, float],
        angle2: float,
        degrees: bool = False
    ) -> Tuple[float, float]:

    Calculates the intersection point of two lines defined by points and angles.

    Parameters
    ----------
    point1 : Tuple[float, float]
        The coordinates of the first point (x, y) through which the first line passes.
    angle1 : float
        The angle of the first line in degrees or radians.
    point2 : Tuple[float, float]
        The coordinates of the second point (x, y) through which the second line passes.
    angle2 : float
        The angle of the second line in degrees or radians.
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).

    Returns
    -------
    * `Tuple[float, float]`
        The coordinates of the intersection point (x, y). (None, None) if the lines are parallel.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_intersection_point((0, 0), 45, (1, 1), 135, degrees=True)
    (1.0, 0.9999999999999999)
    """
    if degrees:
        angle1 = np.radians(angle1)
        angle2 = np.radians(angle2)

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the slopes of the lines
    m1 = np.tan(angle1)
    m2 = np.tan(angle2)

    # lines are parallel so they don't intersect
    if m1 == m2:
        return None, None

    b1 = y1 - m1 * x1
    b2 = y2 - m2 * x2

    intersection_x = float((b2 - b1) / (m1 - m2))
    intersection_y = float(m1 * intersection_x + b1)

    return intersection_x, intersection_y


def draw_segment(
    start: Tuple[float, float],
    end: Tuple[float, float],
    line_width: float = 0.001,
    color: str = "black",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_segment(
        start: Tuple[float, float],
        end: Tuple[float, float],
        line_width: float = 0.001,
        color: str = 'black',
        ax: Optional[plt.Axes] = None
    ) -> None

    Draws a segment between two points with a specified line width and color.

    Parameters
    ----------
    start : Tuple[float, float]
        The coordinates of the starting point (x, y).
    end : Tuple[float, float]
        The coordinates of the final point (x, y).
    line_width : float, optional
        The width of the segment. (Default is 0.001)
    color : str, optional
        The color of the segment. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the segment on. If None, uses the current Axes

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment((0, 0), (1, 1), line_width=0.005, color='blue')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    x_initial, y_initial = start
    x_final, y_final = end
    angle = np.arctan2(y_final - y_initial, y_final - x_initial)
    offset_x = np.sin(angle) * line_width / 2
    offset_y = np.cos(angle) * line_width / 2
    x1 = x_initial + offset_x
    y1 = y_initial - offset_y
    x2 = x_initial - offset_x
    y2 = y_initial + offset_y
    x3 = x_final - offset_x
    y3 = y_final + offset_y
    x4 = x_final + offset_x
    y4 = y_final - offset_y
    plt.fill([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color=color)


def plot_annotate_arrow_end(
    end: Tuple[float, float],
    angle: float,
    length: float,
    degrees: bool = False,
    text: str = "",
    text_offset: float = 0.5,
    fontsize: int = 12,
    text_align: dict = None,
    arrow_props: dict = None,
    reverse: bool = False,
    center_text: bool = False,
    reverse_text: bool = False,
    alpha: float = 0.8,
    ax: Optional[plt.Axes] = None,
) -> tuple[float, float]:
    """
    >>> def plot_annotate_arrow_end(
        end: Tuple[float, float],
        angle: float,
        length: float,
        degrees: bool = False,
        text: str = "",
        text_offset: float = 0.5,
        fontsize: int = 12,
        text_align: dict = None,
        arrow_props: dict = None,
        reverse: bool = False,
        center_text: bool = False,
        reverse_text: bool = False,
        alpha: float = 0.8,
        ax: Optional[plt.Axes] = None,
    ) -> Tuple[float, float]:

    Plots an arrow annotation at the end point of a vector.

    Parameters
    ----------
    end : Tuple[float, float]
        The coordinates of the end point (x, y) of the vector.
    angle : float
        The angle of the vector in degrees or radians.
    length : float
        The length of the vector.
    degrees : bool, optional
        Whether the angle is given in degrees (Default is False).
    text : str, optional
        The text to be displayed near the arrow (Default is "").
    text_offset : float, optional
        The distance between the text and the arrow (Default is 0.5).
    fontsize : int, optional
        The font size of the text (Default is 12).
    text_align : dict, optional
        The text alignment (Default is {'ha': 'center', 'va': 'top'}).
    arrow_props : dict, optional
        The properties of the arrow (Default is {'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'}).
    reverse : bool, optional
        Whether to reverse the arrow (Default is False).
    center_text : bool, optional
        Whether to place the text in the center (Default is False).
    reverse_text : bool, optional
        Whether to reverse the text (Default is False).
    alpha : float, optional
        The transparency of the arrow and text (Default is 0.8).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `Tuple[float, float]`
        The coordinates of the start point (x, y) of the arrow.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_annotate_arrow_end((1, 1), 45, 1, text="End", text_offset=0.5, fontsize=12, text_align={'ha': 'center', 'va': 'top'}, degrees=True)
    (10.899494936611665, 10.899494936611665)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    arrow_props = arrow_props or {
        "width": 2,
        "head_width": 15,
        "head_length": 15,
        "fc": "black",
        "ec": "black",
    }
    text_align = text_align or {"ha": "center", "va": "top"}

    start = (
        end[0] - (length - arrow_props["head_length"]) * np.cos(angle),
        end[1] - (length - arrow_props["head_length"]) * np.sin(angle),
    )
    if not reverse:
        ax.arrow(
            *start,
            *(end[0] - start[0], end[1] - start[1]),
            **arrow_props,
            alpha=alpha,
        )
    else:
        start = (
            end[0] - length * np.cos(angle),
            end[1] - length * np.sin(angle),
        )
        ax.arrow(
            *end,
            *(start[0] - end[0], start[1] - end[1]),
            **arrow_props,
            alpha=alpha,
        )

    mid = (
        start[0] + 0.5 * length * np.cos(angle),
        start[1] + 0.5 * length * np.sin(angle),
    )
    if not center_text:
        ax.text(
            start[0] - text_offset * np.cos(angle),
            start[1] - text_offset * np.sin(angle),
            text,
            fontsize=fontsize,
            color="k",
            **text_align,
        )
    else:
        rot_angle = -angle if angle < np.pi / 2 else (np.pi - angle)
        rot_angle = rot_angle + np.pi if reverse_text else rot_angle
        ax.text(
            mid[0] + text_offset * np.cos(np.pi / 2 + angle),
            mid[1] + text_offset * np.sin(np.pi / 2 + angle),
            text,
            fontsize=fontsize,
            color="k",
            **text_align,
            rotation=rot_angle,
        )

    return tuple(map(float, start))


def draw_arc_with_text(
    center: Tuple[float, float],
    radius: float,
    start_angle: float,
    end_angle: float,
    text: str = "",
    degrees: bool = False,
    text_offset: float = 0.7,
    fontsize: int = 8,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_arc_with_text(
        center: Tuple[float, float],
        radius: float,
        start_angle: float,
        end_angle: float,
        text: str = "",
        degrees: bool = False,
        text_offset: float = 0.7,
        fontsize: int = 8,
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws an arc with text annotation.

    Parameters
    ----------
    center : Tuple[float, float]
        The coordinates (x, y) of the center point of the circle from which the arc is drawn.
    radius : float
        The radius of the arc.
    start_angle : float
        The start angle of the arc in degrees or radians.
    end_angle : float
        The end angle of the arc in degrees or radians.
    text : str
        The text to be displayed along the arc.
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).
    text_offset : float, optional
        The distance factor from the arc center to position the text (Default is 0.7).
    fontsize : int, optional
        The font size of the text (Default is 8).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_arc_with_text((0, 0), 5, 30, 120, "Sample Text", degrees=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        start_angle = np.radians(start_angle)
        end_angle = np.radians(end_angle)

    # Normalize angles to [0, 2*pi)
    start_angle = start_angle % (2 * np.pi)
    end_angle = end_angle % (2 * np.pi)

    angles = np.linspace(start_angle, end_angle, 1000)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    ax.plot(x, y, color="black", linewidth=1)

    mid_angle = (start_angle + end_angle) / 2
    text_x = center[0] + radius * np.cos(mid_angle) * (1 + text_offset)
    text_y = center[1] + radius * np.sin(mid_angle) * (1 + text_offset)

    ax.text(
        text_x,
        text_y,
        text,
        fontsize=fontsize,
        ha="center",
        va="center",
    )
    ax.axis("equal")


def draw_three_axes_rotated(
    arrow_length: float,
    line_thickness: float = 1.5,
    text_offset: float = 0.2,
    longx: float = 1,
    negativeaxis_y: bool = False,
    negativeaxis_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> draw_three_axes_rotated(
        arrow_length: float,
        line_thickness: float = 1.5,
        text_offset: float = 0.2,
        longx: float = 1,
        negativeaxis_y: bool = False,
        negativeaxis_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes

    Draws three rotated axes in a 3D coordinate system.

    Parameters
    ----------
    arrow_length : float
        The length of the arrow.
    line_thickness : float
        The thickness of the line. (Default is 1.5)
    text_offset : float
        The offset of the text from the arrow. (Default is 0.2)
    longx : float
        The length of the x-axis. (Default is 1)
    negativeaxis_y : bool
        Whether to include negative y-axis (default is False).
    negativeaxis_x : bool
        Whether to include negative x-axis (default is False).
    ax : Optional[plt.Axes], optional
        The Axes object to draw the plot on. If None, uses the current Axes.

    Returns
    -------
    * `plt.Axes` :
        The matplotlib Axes object containing the plot.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_three_axes_rotated(arrow_length=1.0, negativeaxis_y=True, negativeaxis_x=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    angle = np.radians(30)

    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(0, arrow_length + text_offset, "z", fontsize=12, ha="center", va="bottom")

    ax.arrow(
        0,
        0,
        -arrow_length * np.cos(angle) / longx,
        -arrow_length * np.sin(angle) / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        -arrow_length * np.cos(angle) / longx - text_offset,
        -arrow_length * np.sin(angle) / longx - text_offset,
        "x",
        fontsize=12,
        ha="left",
        va="center",
    )

    if negativeaxis_x:
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(angle) / longx,
            arrow_length * np.sin(angle) / longx,
            head_width=0,
            head_length=0,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(angle) / longx,
            -arrow_length * np.sin(angle) / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.text(
            arrow_length * np.cos(angle) / longx + 2 * text_offset / 1.5,
            -arrow_length * np.sin(angle) / longx - text_offset / 1.5,
            "y",
            fontsize=12,
            ha="right",
            va="top",
        )

    if negativeaxis_y:
        ax.arrow(
            0,
            0,
            -arrow_length * np.cos(angle) / longx,
            arrow_length * np.sin(angle) / longx,
            head_width=0,
            head_length=0,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


def draw_double_arrowhead(
    start: Tuple[float, float],
    end: Tuple[float, float],
    color: str = "black",
    line_thickness: float = 1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_double_arrowhead(
        start: Tuple[float, float],
        end: Tuple[float, float],
        color: str = 'black',
        line_thickness: float = 1
        ax: Optional[plt.Axes] = None
    ) -> None

    Draws a double arrowhead between two points.

    Parameters
    ----------
    start : Tuple[float, float]
        Coordinates of the start point (x, y).
    end : Tuple[float, float]
        Coordinates of the end point (x, y).
    color : str, optional
        Color of the arrow and line. (Default is 'black')
    line_thickness : float, optional
        Thickness of the line. (Default is 1)
    ax : Optional[plt.Axes], optional
        The Axes object to draw the plot on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_double_arrowhead(start=(0, 0), end=(1, 1))
    >>> plt.show()
    """
    ax = ax or plt.gca()

    start = list(start)
    end = list(end)
    modified_start = start.copy()
    modified_end = end.copy()
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    modified_start[0] += 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_start[1] += 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    modified_end[0] -= 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_end[1] -= 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    dx = modified_end[0] - modified_start[0]
    dy = modified_end[1] - modified_start[1]
    plt.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_start[0],
        modified_start[1],
        dx,
        dy,
        head_width=0.05,
        head_length=0.08,
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_end[0],
        modified_end[1],
        -dx,
        -dy,
        head_width=0.05,
        head_length=0.08,
        color=color,
        linewidth=line_thickness,
    )


def draw_custom_arrow_end(
    start: Tuple[float, float],
    end: Tuple[float, float],
    color: str = "black",
    line_thickness: float = 1,
) -> None:
    """
    >>> draw_custom_arrow_end(
        start: tuple,
        end: tuple,
        color: str = 'black',
        line_thickness: float = 1
    ) -> None

    Draws a custom arrow at the end of a line segment.

    Parameters
    ----------
    start : Tuple[float, float]
        Coordinates of the start point (x, y).
    end : Tuple[float, float]
        Coordinates of the end point (x, y).
    color : str, optional
        Color of the arrow and line. (Default is 'black')
    line_thickness : float, optional
        Thickness of the line. (Default is 1)

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_custom_arrow_end(start=(0, 0), end=(1, 1), color='black', line_thickness=1)
    >>> plt.show()
    """
    start = list(start)
    end = list(end)
    modified_start = start.copy()
    modified_end = end.copy()
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    modified_start[0] += 10 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_start[1] += 10 * dy / ((dx**2 + dy**2) ** 0.5)
    modified_end[0] -= 10 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_end[1] -= 10 * dy / ((dx**2 + dy**2) ** 0.5)
    dx = modified_end[0] - modified_start[0]
    dy = modified_end[1] - modified_start[1]
    plt.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_start[0],
        modified_start[1],
        dx,
        dy,
        head_width=10,
        head_length=10,
        color=color,
        linewidth=line_thickness,
    )


def draw_two_axes(
    arrow_length: float,
    line_thickness: float = 1.5,
    text_offset: float = 0.1,
    longx: float = 1,
    negativeaxis_y: bool = False,
    negativeaxis_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_two_axes(
        arrow_length: float,
        line_thickness: float = 1.5,
        text_offset: float = 0.1,
        longx: float = 1,
        negativeaxis_y: bool = False,
        negativeaxis_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws two axes representing the x and y directions.

    Parameters
    ----------
    arrow_length : float
        Length of the arrows representing the axes.
    line_thickness : float, optional
        Thickness of the arrows representing the axes. (Default is 1.5)
    text_offset : float, optional
        Offset for the axis labels. (Default is 0.1)
    longx : float, optional
        Length factor for the x-axis.
    negativeaxis_y : bool, optional
        Indicating whether to draw the negative y-axis.
    negativeaxis_x : bool, optional
        Indicating whether to draw the negative x-axis.

    Returns
    -------
    * `plt.Axes` :
        Axes object.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_two_axes(arrow_length=1.0, negativeaxis_y=True, negativeaxis_x=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(0, arrow_length + text_offset, "y", fontsize=12, ha="center", va="bottom")

    if negativeaxis_y:
        ax.arrow(
            0,
            0,
            0,
            -arrow_length,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.arrow(
        0,
        0,
        longx * arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        longx * arrow_length + text_offset, 0, "x", fontsize=12, ha="left", va="center"
    )

    if negativeaxis_x:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


import matplotlib.pyplot as plt
from typing import Tuple


def vertical_arrow_rain(
    quantity_arrows: int,
    start: Tuple[float, float],
    end: Tuple[float, float],
    y_origin: float = 0,
    arrow_color: str = "blue",
    head_width: float = 0.05,
    head_length: float = 0.1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def vertical_arrow_rain(
        quantity_arrows: int,
        start: Tuple[float, float],
        end: Tuple[float, float],
        y_origin: float = 0,
        arrow_color: str = "blue",
        head_width: float = 0.05,
        head_length: float = 0.1,
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws a specific quantity of arrows from equidistant points on a segment that extends from start to end,
    with all arrows pointing to y_origin.

    Parameters
    ----------
    quantity_arrows : int
        Number of arrows to draw.
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point of the segment.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point of the segment.
    y_origin : float, optional
        y-coordinate to which all arrows should point. Default is 0.
    arrow_color : str, optional
        Color of the arrows. Default is "blue".
    head_width : float, optional
        Width of the arrow heads. Default is 0.05.
    head_length : float, optional
        Length of the arrow heads. Default is 0.1.
    ax : Optional[plt.Axes], optional

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> vertical_arrow_rain(quantity_arrows=5, start=(0, 1), end=(1, 1), y_origin=0)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    if quantity_arrows < 2:
        raise ValueError("quantity_arrows must be at least 2.")

    x_initial, y_initial = start
    x_final, y_final = end

    x_points = [
        x_initial + i * (x_final - x_initial) / (quantity_arrows - 1)
        for i in range(quantity_arrows)
    ]
    y_points = [
        y_initial + i * (y_final - y_initial) / (quantity_arrows - 1)
        for i in range(quantity_arrows)
    ]

    for x, y in zip(x_points, y_points):
        plt.arrow(
            x,
            y,
            0,
            y_origin - y,
            head_width=head_width,
            head_length=head_length,
            fc=arrow_color,
            ec=arrow_color,
        )


def draw_rain_arrows_horizontal(
    quantity_arrows: int,
    start: Tuple[float, float],
    end: Tuple[float, float],
    x_origin: float = 0,
    arrow_color: str = "blue",
    head_width: float = 0.05,
    head_length: float = 0.1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def draw_rain_arrows_horizontal(
        quantity_arrows: int,
        start: Tuple[float, float],
        end: Tuple[float, float],
        x_origin: float = 0,
        arrow_color: str = "blue",
        head_width: float = 0.05,
        head_length: float = 0.1,
        ax: Optional[plt.Axes] = None,
    ) -> None:

    Draws a specific quantity of arrows from a vertical line at x_origin to equidistant points on a segment that extends from start to end.

    Parameters
    ----------
    quantity_arrows : int
        Number of arrows to draw.
    x_origin : float
        x-coordinate from which all arrows originate.
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point of the segment.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point of the segment.
    arrow_color : str, optional
        Color of the arrows. Default is "blue".
    head_width : float, optional
        Width of the arrow heads. Default is 0.05.
    head_length : float, optional
        Length of the arrow heads. Default is 0.1.
    ax : Optional[plt.Axes], optional
        The Axes object to draw the plot on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_rain_arrows_horizontal(quantity_arrows=5, start=(0, 1), end=(1, 1))
    >>> plt.show()
    """
    if quantity_arrows < 2:
        raise ValueError("quantity_arrows must be at least 2.")

    ax = ax or plt.gca()

    x_initial, y_initial = start
    x_final, y_final = end
    y_points = [
        y_initial + i * (y_final - y_initial) / (quantity_arrows - 1)
        for i in range(quantity_arrows)
    ]

    for y in y_points:
        ax.arrow(
            x_origin,
            y,
            x_initial - x_origin,
            0,
            head_width=head_width,
            head_length=head_length,
            fc=arrow_color,
            ec=arrow_color,
        )


def calculate_angle(
    start: Tuple[float, float], end: Tuple[float, float], degrees: bool = False
) -> float:
    """
    >>> calculate_angle(
        start: Tuple[float, float],
        end: Tuple[float, float]
    ) -> float

    Calculates the angle between two points.

    Parameters
    ----------
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point.
    degrees : bool, optional
        Whether to return the angle in degrees (Default is False).

    Returns
    -------
    * `float` :
        The angle between the two points.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_angle(start=(0, 0), end=(1, 1), degrees=True)
    45.0
    """
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    angle_rad = math.atan2(delta_y, delta_x)

    # normalize angle to [0, 2*pi)
    angle_rad = angle_rad % (2 * math.pi)

    return math.degrees(angle_rad) if degrees else angle_rad


def draw_segment_1(start: Tuple[float, float], end: Tuple[float, float]) -> None:
    """
    >>> draw_segment_1(
        start: Tuple[float, float],
        end: Tuple[float, float]
    ) -> None

    Draws a line segment in black ('k').

    Parameters
    ----------
    start : Tuple[float, float]
        The coordinates of the starting point [x1, y1].
    end : Tuple[float, float]
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_1((0, 0), (10, 0))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="k")


def draw_segment_2(start: Union[tuple, list], end: Union[tuple, list]) -> None:
    """
    >>> draw_segment_2(
        start: Union[tuple, list],
        end: Union[tuple, list]
    ) -> None

    Draws a line segment in red ('r').

    Parameters
    ----------
    start : Tuple[float, float]
        The coordinates of the starting point [x1, y1].
    end : Tuple[float, float]
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as pltdraw
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_2((0, 2.6), (10, 1))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="r")


def draw_segment_3(start: Tuple[float, float], end: Tuple[float, float]) -> None:
    """
    >>> draw_segment_3(
        start: Tuple[float, float],
        end: Tuple[float, float]
    ) -> None

    Draws a line segment in blue ('b').

    Parameters
    ----------
    start : tuple or list
        The coordinates of the starting point [x1, y1].
    end : tuple or list
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_3((0, 2.6), (10, 1))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="b")


def get_arc_points(
    start_angle: float,
    end_angle: float,
    radius: float,
    center: Tuple[float, float] = (0, 0),
    degrees: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculates points along a circular arc defined by a start angle and an end angle.

    Parameters
    ----------
    start_angle : float
        The starting angle of the arc in degrees or radians.
    end_angle : float
        The ending angle of the arc in degrees or radians.
    radius : float
        The radius of the arc.
    center : Tuple[float, float], optional
        The coordinates of the center of the arc [cx, cy]. (Default is (0, 0))
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).

    Returns
    -------
    * `Tuple[np.ndarray, np.ndarray]`
        The x and y coordinates of the arc points.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> arc_points_x1, arc_points_y1 = pltdraw.get_arc_points(90, 240, 0.25, (0, -0.25), degrees=True)
    >>> plt.plot(arc_points_x1, arc_points_y1, 'k')
    >>> plt.show()
    """
    if degrees:
        start_angle = np.radians(start_angle)
        end_angle = np.radians(end_angle)

    angles = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


__all__ = [
    "draw_arrow",
    "calculate_midpoint",
    "draw_arc",
    "create_blank_canvas",
    "draw_three_axes",
    "draw_two_inclined_axes",
    "plot_line_segment",
    "plot_annotate_arrow",
    "draw_custom_arrow",
    "calculate_arrow_endpoint_pixels",
    "plot_segment",
    "plot_segment_dashed",
    "draw_custom_circle",
    "draw_rounded_rectangle",
    "calculate_intersection_point",
    "draw_segment",
    "plot_annotate_arrow_end",
    "draw_arc_with_text",
    "draw_three_axes_rotated",
    "draw_double_arrowhead",
    "draw_custom_arrow_end",
    "draw_two_axes",
    "vertical_arrow_rain",
    "draw_rain_arrows_horizontal",
    "calculate_angle",
    "draw_segment_1",
    "draw_segment_2",
    "draw_segment_3",
    "get_arc_points",
]
