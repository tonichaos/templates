import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QWidget, QVBoxLayout, QPushButton, \
    QMessageBox
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt


class CIDTemplateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operations Template")
        self.setGeometry(100, 100, 600, 800)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the central widget
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create labels
        self.casefile_label = QLabel("(Maximize the app first to see full)\nUndercover operations", self)
        self.layout.addWidget(self.casefile_label)

        self.agent_info_label = QLabel("Agent Information", self)
        self.layout.addWidget(self.agent_info_label)

        self.date_label = QLabel("Date of Operation", self)
        self.layout.addWidget(self.date_label)

        self.date_line_edit = QLineEdit(self)
        self.layout.addWidget(self.date_line_edit)

        self.operating_agent_label = QLabel("Operating Agent(s)", self)
        self.layout.addWidget(self.operating_agent_label)

        self.operating_agent_text_edit = QTextEdit(self)
        self.layout.addWidget(self.operating_agent_text_edit)

        self.suspect_info_label = QLabel("Suspect Information", self)
        self.layout.addWidget(self.suspect_info_label)

        self.full_name_label = QLabel("Full Name", self)
        self.layout.addWidget(self.full_name_label)

        self.full_name_line_edit = QLineEdit(self)
        self.layout.addWidget(self.full_name_line_edit)

        self.phone_number_label = QLabel("Suspect's Phone Number", self)
        self.layout.addWidget(self.phone_number_label)

        self.phone_number_line_edit = QLineEdit(self)
        self.layout.addWidget(self.phone_number_line_edit)

        self.photo_of_the_suspect_label = QLabel("Photograph of the suspect", self)
        self.layout.addWidget(self.photo_of_the_suspect_label)

        self.photo_of_the_suspect_line_edit = QLineEdit(self)
        self.layout.addWidget(self.photo_of_the_suspect_line_edit)

        self.operations_label = QLabel("Operation Information", self)
        self.layout.addWidget(self.operations_label)

        self.operation_type_label = QLabel("Operation Type:", self)
        self.layout.addWidget(self.operation_type_label)

        self.operation_type_edit = QLineEdit(self)
        self.layout.addWidget(self.operation_type_edit)

        self.number_of_sus = QLabel("Number of Suspects:", self)
        self.layout.addWidget(self.number_of_sus)

        self.number_of_sus_edit = QLineEdit(self)
        self.layout.addWidget(self.number_of_sus_edit)

        self.charges_label = QLabel("Charges:", self)
        self.layout.addWidget(self.charges_label)

        self.charges_edit = QLineEdit(self)
        self.layout.addWidget(self.charges_edit)

        self.photo_video_proof_label = QLabel("Photographic and /or video - recorded evidence")
        self.layout.addWidget(self.photo_video_proof_label)

        self.meeting_n_deal_label = QLabel("The meeting and deal:")
        self.layout.addWidget(self.meeting_n_deal_label)

        self.meeting_n_deal_edit = QLineEdit(self)
        self.layout.addWidget(self.meeting_n_deal_edit)

        self.proof_of_distribute_label = QLabel("Evidence of suspect distributing illegal stuff:")
        self.layout.addWidget(self.proof_of_distribute_label)

        self.proof_of_distribute_edit = QLineEdit(self)
        self.layout.addWidget(self.proof_of_distribute_edit)

        self.confiscation_of_illegal_stuff_label = QLabel("Confiscation of illegal stuff from the suspect:")
        self.layout.addWidget(self.confiscation_of_illegal_stuff_label)

        self.confiscation_of_illegal_stuff_edit = QLineEdit(self)
        self.layout.addWidget(self.confiscation_of_illegal_stuff_edit)

        self.pressing_charges_label = QLabel("Pressing Charges followed by his arrest:")
        self.layout.addWidget(self.pressing_charges_label)


        self.pressing_charges_edit = QLineEdit(self)
        self.layout.addWidget(self.pressing_charges_edit)

        self.dropping_label = QLabel("Dropping the confiscated illegal stuff into the FBI Dropbox:")
        self.layout.addWidget(self.dropping_label)

        self.dropping_edit = QLineEdit(self)
        self.layout.addWidget(self.dropping_edit)

        self.background_check_label = QLabel("Background Check:")
        self.layout.addWidget(self.background_check_label)

        self.background_check_edit = QLineEdit(self)
        self.layout.addWidget(self.background_check_edit)

        # Create a button to generate the template
        self.generate_template_button = QPushButton("Generate Template", self)
        self.generate_template_button.clicked.connect(self.generate_template)
        self.layout.addWidget(self.generate_template_button)

    def generate_template(self):
        # Get the values from the input boxes
        date = self.date_line_edit.text()
        operating_agents = self.operating_agent_text_edit.toPlainText()
        full_name = self.full_name_line_edit.text()
        phone_number = self.phone_number_line_edit.text()
        photo_of_the_suspect = self.photo_of_the_suspect_line_edit.text()
        number_of_sus = self.number_of_sus_edit.text()
        operation_type = self.operation_type_edit.text()
        meeting_n_deal = self.meeting_n_deal_edit.text()
        evidence_of_sus_distribute = self.proof_of_distribute_edit.text()
        confiscation_of_illegal_stuff = self.confiscation_of_illegal_stuff_edit.text()
        pressing_charges = self.pressing_charges_edit.text()
        dropping_the_stuff = self.dropping_edit.text()
        charges = self.charges_edit.text()
        background_check = self.background_check_edit.text()

        # Create the template with BBCodes and
        template = f"[CENTER][IMG]https://i.imgur.com/ndAN0Ss.png?1[/IMG]\n[FONT=Century Gothic][COLOR=#FFFFFF][SIZE=5]Undercover Operation\n[/SIZE][/COLOR][/FONT][IMG]https://i.imgur.com/5Iceuzj.png[/IMG][/CENTER]\n\n[SIZE=4][U]Agent(s) Information[/U][/SIZE]\n\n[B]Date of Operation[/B]\n[INDENT]{date}[/INDENT]\n\n[B]Operating Agent(s)[/B]\n[INDENT][list][*]{operating_agents}[/list][/INDENT]\n\n[SIZE=4][U]Suspect(s) Information[/U][/SIZE]\n\n[B]Suspect Name(s):[/B]\n[INDENT]{full_name}[/INDENT]\n\n[B]Suspect's Phone Number:[/B]\n[INDENT]{phone_number}[/INDENT]\n\n[B]Photograph of the Suspect:[/B]\n[INDENT]{photo_of_the_suspect}[/INDENT]\n\n[B]Background check:[/B]\n[INDENT][spoiler]{background_check}[/spoiler][/INDENT]\n\n[SIZE=4][U]Operation Information[/U][/SIZE]\n\n[B]Operation's type[/B]\n[INDENT]{operation_type}[/INDENT]\n\n[B]Number of suspects[/B]\n[INDENT]{number_of_sus}[/INDENT]\n\n[I][B]Charges[/B][/I]\n[INDENT][list][*]{charges}[/LIST][/INDENT]\n\n[B]Photographic and/or video-recorded evidence[/B]\n[spoiler]\n\nThe meeting and deal  :\n[spoiler]{meeting_n_deal}[/spoiler]\n\nEvidence of suspect distributing illegal stuff :\n[Spoiler]{evidence_of_sus_distribute}[/spoiler]\n\nConfiscation of illegal stuff from the suspect :\n[Spoiler]{confiscation_of_illegal_stuff}[/spoiler]\n\nPressing Charges followed by his arrest :\n[Spoiler]{pressing_charges}[/spoiler]\n\nDropping the confiscated stuff into the FBI Dropbox\n[Spoiler]{dropping_the_stuff}[/spoiler][/spoiler][INDENT][/INDENT]"
        # Copy the template to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(template, mode=QClipboard.Clipboard)

        # Show a message box to inform the user
        QMessageBox.information(self, "Template Generated", "The template has been generated and copied to the "
                                                            "clipboard.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CIDTemplateApp()
    window.show()
    sys.exit(app.exec_())
