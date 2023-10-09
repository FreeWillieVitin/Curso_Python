"""
QSS - Estilos do QT for Python
https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
Dark Theme
https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
"""
import qdarktheme
from var import PRIMARY_COLOR, ESCURA_PRIMARY_COLOR, MAIS_ESCURA_PRIMARY_COLOR

qss = f"""
    Button[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    Button[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {ESCURA_PRIMARY_COLOR};
    }}
    Button[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {MAIS_ESCURA_PRIMARY_COLOR};
    }}
"""


def setupTheme(tema):
    qdarktheme.setup_theme(
        theme=tema,
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": "#1e81b0"
            },
            "[light]": {
                "primary": "#1e81b0"
            },
        },
        additional_qss=qss
    )
