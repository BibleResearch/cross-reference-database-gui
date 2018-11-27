from django.test import TestCase

# Create your tests here.



# class CrossReferenceTests(TestCase):
#     """Email related tests."""

#     def test_importer_simply(self):
#         new_email = TestData.create_email()
#         assert new_email.id == '72f3db3208c69b13abf40e7694c37e850a0a4b9499ab737670c630387df02eb8'

#     def test_create_email(self):
#         """Test email creation."""
#         new_email = TestData.create_email()
#         assert new_email.id == TestData.email_id
#         assert new_email.full_text == TestData.email_text.replace('\n', '\r\n').strip()
#         relater.date_test(new_email.first_seen)
#         relater.date_test(new_email.modified)
#         assert len(new_email.submitter) == 16

#     def test_create_empty_email(self):
#         """Test email creation."""
#         new_email = TestData.create_email('')
#         assert new_email is None

#     def test_related_bodies(self):
#         """Make sure a header and body are related to a created email."""
#         new_email = TestData.create_email()
#         assert len(new_email.bodies.all()) == 2
#         body_ids = [body.id for body in new_email.bodies.all()]
#         assert '8e87067dacf77be7daa2910c6b525dddaff3e51bb0c75b5118922a02794dd578' in body_ids
#         assert 'da39ab5b4dd6e13df2b2a51e050368c6517fa438d23257d63a3fca57f8cab6ad' in body_ids

#     def test_related_header_body_and_attachment(self):
#         """Make sure a header and body are related to a created email."""
#         created_content = TestData.create_email(TestData.attachment_email_text)
#         new_email = created_content
#         new_header = created_content.header
#         new_attachments = created_content.attachments.all()
#         new_attachment_ids = [attachment.id for attachment in new_attachments]

#         assert new_email.header.id == new_header.id
#         assert len(new_email.attachments.all()) == len(new_attachments)

#         for attachment in new_attachments:
#             assert attachment.id in new_attachment_ids

#     def test_creating_almost_duplicate_attachments(self):
#         """Make sure TE can handle a situation in which the hash of an attachment already exists, but the name or other details of the attachment have changed."""
#         original_file_name = 'Untitled Diagram.xml'
#         updated_file_name = 'Bingo.xml'
#         new_email = TestData.create_email(TestData.attachment_email_text)
#         assert new_email.attachments.all()[0].filename == original_file_name
#         new_email = TestData.create_email(TestData.attachment_email_text.replace(original_file_name, updated_file_name))
#         assert new_email.attachments.all()[0].filename == 'Untitled Diagram.xml|||Bingo.xml'

#     def test_body_parsing(self):
#         """Make sure a header and body are related to a created email."""
#         created_content = TestData.create_email(TestData.attachment_email_text)
#         new_email = created_content
#         new_bodies = created_content.bodies.all()

#         assert len(new_bodies) == 2
#         assert len(new_email.bodies.all()) == len(new_bodies)

#     def test_bad_body_parsing(self):
#         """Test parsing body from email which is badly parsed."""
#         created_content = TestData.create_email(TestData.bad_body_email_text)
#         assert 'From: pamela4701@eudoramail.com' not in created_content.bodies.all()[0].full_text

#     def test_no_header(self):
#         """Test importing an email with no header."""
#         # There may be an issue if there is an email body uploaded with a url in it (e.g. https://github.com/test/bingo.php)
#         email_text = """
#         This email has no headers!

#         Yours truly,

#         Bob"""
#         new_email = TestData.create_email(email_text)
#         assert new_email.header.full_text == ''

#     def test_email_str(self):
#         """Test email string."""
#         new_email = TestData.create_email()
#         relater.string_test(new_email, TestData.email_id)

#     def test_email_first_seen_modified(self):
#         """Test email first seen date."""
#         new_email = TestData.create_email()
#         # test to make sure that the first_seen date is accurate
#         relater.date_test(new_email.first_seen)
#         # test to make sure that the modified date is accurate
#         relater.date_test(new_email.modified)
#         # make sure that the first seen and modified dates are the same
#         relater.date_test(new_email.first_seen, new_email.modified)
#         # make sure that the hour of the first seen and modified dates are the same
#         assert new_email.first_seen.hour == new_email.modified.hour

#     def test_creation_of_duplicate_email(self):
#         """Test the creation of the same email twice."""
#         new_email1 = TestData.create_email()
#         new_email2 = TestData.create_email()
#         assert new_email1.id == new_email2.id
#         assert new_email1.first_seen == new_email2.first_seen
#         assert new_email1.modified != new_email2.modified

#     def test_line_endings_handling(self):
#         """Make sure two emails with different line endings (in this case `\r\n` and `\n`) are treated as the same email."""
#         lf_id = TestData.create_email(TestData.lf_ending_email_text).id
#         cr_lf_id = TestData.create_email(TestData.cr_lf_ending_email_text).id
#         assert lf_id == cr_lf_id

#     def test_outlook_email_handling(self):
#         """Make sure we can upload emails from outlook."""
#         new_email = TestData.create_email(TestData.outlook_email_text)
#         assert new_email.id == '9f264741172861932af477cc5ef3c24be4ea35301fbb660982cb06bdf0bb6a1d'
#         assert '[173.66.144.161]' in new_email.header.full_text
