################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

class Style():

    style_bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 26px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 26px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 26px solid rgb(85, 170, 255);
    }
    """
    )
    style_bt_delet_row = (
    """
    QPushButton {
        background-position: center;
        background-repeat: no-repeat;
        border: none;
        background-color: rgb(44, 49, 60);
        text-align: left;
        border-radius: 5px;
        text-align: center;
        margin-top: 2px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
    }
    """
    )

    style_LineEdit = (
    """
    QLineEdit {
    	background-color: rgb(27, 29, 35);
    	border-radius: 10px;
    	border: 2px solid rgb(27, 29, 35);
    	padding-left: 10px;
    }
    QLineEdit:hover {
    	border: 2px solid rgb(64, 71, 88);
    }
    QLineEdit:focus {
    	border: 2px solid rgb(91, 101, 124);
    }
    """
    )

    style_LineEdit_empyt = (
    """
    QLineEdit {
    	background-color: rgb(27, 29, 35);
    	border-radius: 10px;
    	border: 2px solid rgb(255, 0, 127);
    	padding-left: 10px;
        color: rgb(255, 0, 127);
    }
    QLineEdit:hover {
    	border: 2px solid rgb(255, 0, 127);
    }
    QLineEdit:focus {
    	border: 2px solid rgb(91, 101, 124);
        color: rgb(210, 210, 210);
    }
    """
    )
