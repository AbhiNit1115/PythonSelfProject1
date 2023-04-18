class PreClinicalStage:
    # Subsystem 1

    def pre_clinical_analysis(self):
        print("The R&D for vaccine is done at this stage")


class ClinicalDevelopment:
    # Subsystem 2

    def clinical_trails(self):
        print("The trails on animals and humans are done at this stage")


class RegulatoryApproval:
    # Subsystem 3

    def review_andapprovals(self):
        print("The appropriate approvals are taken at this stage")


class Manufacturing:
    # Subsystem 4

    def create_vaccine(self):
        print("Actual vaccine creation happens at this stage")


class QualityControl:
    # Subsystem 5

    def test_and_release(self):
        print("the quality check of vaccines are done at this stage")


class VaccineCompany:
    """ This ia a Façade interface of complex patterns that contains several sub-system"""

    def __init__(self):
        self.pre_clinical_stage = PreClinicalStage()
        self.clinical_development = ClinicalDevelopment()
        self.regulatory_approval = RegulatoryApproval()
        self.manufacturing = Manufacturing()
        self.quality_control = QualityControl()

    def create_and_release_vaccine(self):
        self.pre_clinical_stage.pre_clinical_analysis()
        self.clinical_development.clinical_trails()
        self.regulatory_approval.review_andapprovals()
        self.manufacturing.create_vaccine()
        self.quality_control.test_and_release()


vc = VaccineCompany()
vc.create_and_release_vaccine()

