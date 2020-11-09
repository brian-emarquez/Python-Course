'''
/********************************************************************************
** Form generated from reading UI file 'gui_base_oldwySOHy.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/
'''

#ifndef GUI_BASE_OLDWYSOHY_H
#define GUI_BASE_OLDWYSOHY_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QFrame *top_bar;
    QHBoxLayout *horizontalLayout;
    QFrame *frame_toggle;
    QVBoxLayout *verticalLayout_2;
    QPushButton *Btn_Toogle;
    QFrame *frame_top;
    QFrame *content;
    QHBoxLayout *horizontalLayout_2;
    QFrame *frame_left_menu;
    QVBoxLayout *verticalLayout_3;
    QFrame *frame_top__menus;
    QVBoxLayout *verticalLayout_4;
    QPushButton *Btn_Menu_2;
    QPushButton *Btn_Menu_1;
    QPushButton *Btn_Menu_3;
    QFrame *frame_pages;
    QVBoxLayout *verticalLayout_5;
    QStackedWidget *Pages_Widget;
    QWidget *page;
    QWidget *page_2;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1000, 500);
        MainWindow->setMaximumSize(QSize(1000, 500));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        centralwidget->setStyleSheet(QStringLiteral("background-color: rgb(45, 45, 45);"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        top_bar = new QFrame(centralwidget);
        top_bar->setObjectName(QStringLiteral("top_bar"));
        top_bar->setMaximumSize(QSize(16777215, 40));
        top_bar->setStyleSheet(QStringLiteral("background-color: rgb(35, 35, 35);"));
        top_bar->setFrameShape(QFrame::NoFrame);
        top_bar->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(top_bar);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        frame_toggle = new QFrame(top_bar);
        frame_toggle->setObjectName(QStringLiteral("frame_toggle"));
        frame_toggle->setMaximumSize(QSize(70, 40));
        frame_toggle->setStyleSheet(QStringLiteral("background-color: rgb(85, 170, 255);"));
        frame_toggle->setFrameShape(QFrame::StyledPanel);
        frame_toggle->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame_toggle);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        Btn_Toogle = new QPushButton(frame_toggle);
        Btn_Toogle->setObjectName(QStringLiteral("Btn_Toogle"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Btn_Toogle->sizePolicy().hasHeightForWidth());
        Btn_Toogle->setSizePolicy(sizePolicy);
        Btn_Toogle->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
"border: 0 px solid;"));

        verticalLayout_2->addWidget(Btn_Toogle);


        horizontalLayout->addWidget(frame_toggle);

        frame_top = new QFrame(top_bar);
        frame_top->setObjectName(QStringLiteral("frame_top"));
        frame_top->setMaximumSize(QSize(16777215, 40));
        frame_top->setFrameShape(QFrame::StyledPanel);
        frame_top->setFrameShadow(QFrame::Raised);

        horizontalLayout->addWidget(frame_top);


        verticalLayout->addWidget(top_bar);

        content = new QFrame(centralwidget);
        content->setObjectName(QStringLiteral("content"));
        content->setFrameShape(QFrame::NoFrame);
        content->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(content);
        horizontalLayout_2->setSpacing(0);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        frame_left_menu = new QFrame(content);
        frame_left_menu->setObjectName(QStringLiteral("frame_left_menu"));
        frame_left_menu->setMinimumSize(QSize(70, 0));
        frame_left_menu->setMaximumSize(QSize(70, 16777215));
        frame_left_menu->setStyleSheet(QStringLiteral("background-color: rgb(35, 35, 35);"));
        frame_left_menu->setFrameShape(QFrame::StyledPanel);
        frame_left_menu->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(frame_left_menu);
        verticalLayout_3->setSpacing(0);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        frame_top__menus = new QFrame(frame_left_menu);
        frame_top__menus->setObjectName(QStringLiteral("frame_top__menus"));
        frame_top__menus->setFrameShape(QFrame::NoFrame);
        frame_top__menus->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(frame_top__menus);
        verticalLayout_4->setSpacing(0);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        Btn_Menu_2 = new QPushButton(frame_top__menus);
        Btn_Menu_2->setObjectName(QStringLiteral("Btn_Menu_2"));
        Btn_Menu_2->setMinimumSize(QSize(0, 40));
        Btn_Menu_2->setStyleSheet(QLatin1String("QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}"));

        verticalLayout_4->addWidget(Btn_Menu_2);

        Btn_Menu_1 = new QPushButton(frame_top__menus);
        Btn_Menu_1->setObjectName(QStringLiteral("Btn_Menu_1"));
        Btn_Menu_1->setMinimumSize(QSize(0, 40));
        Btn_Menu_1->setStyleSheet(QLatin1String("QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}"));

        verticalLayout_4->addWidget(Btn_Menu_1);

        Btn_Menu_3 = new QPushButton(frame_top__menus);
        Btn_Menu_3->setObjectName(QStringLiteral("Btn_Menu_3"));
        Btn_Menu_3->setMinimumSize(QSize(0, 40));
        Btn_Menu_3->setStyleSheet(QLatin1String("QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}"));

        verticalLayout_4->addWidget(Btn_Menu_3);


        verticalLayout_3->addWidget(frame_top__menus, 0, Qt::AlignTop);


        horizontalLayout_2->addWidget(frame_left_menu);

        frame_pages = new QFrame(content);
        frame_pages->setObjectName(QStringLiteral("frame_pages"));
        frame_pages->setMinimumSize(QSize(0, 0));
        frame_pages->setFrameShape(QFrame::StyledPanel);
        frame_pages->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(frame_pages);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        Pages_Widget = new QStackedWidget(frame_pages);
        Pages_Widget->setObjectName(QStringLiteral("Pages_Widget"));
        page = new QWidget();
        page->setObjectName(QStringLiteral("page"));
        Pages_Widget->addWidget(page);
        page_2 = new QWidget();
        page_2->setObjectName(QStringLiteral("page_2"));
        Pages_Widget->addWidget(page_2);

        verticalLayout_5->addWidget(Pages_Widget);


        horizontalLayout_2->addWidget(frame_pages);


        verticalLayout->addWidget(content);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        Pages_Widget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        Btn_Toogle->setText(QApplication::translate("MainWindow", "TOOGLE", nullptr));
        Btn_Menu_2->setText(QApplication::translate("MainWindow", "Menu 1", nullptr));
        Btn_Menu_1->setText(QApplication::translate("MainWindow", "Menu 1", nullptr));
        Btn_Menu_3->setText(QApplication::translate("MainWindow", "Menu 1", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GUI_BASE_OLDWYSOHY_H
