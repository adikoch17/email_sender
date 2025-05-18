import streamlit as st
from streamlit_quill import st_quill
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "aditya.tempbs@gmail.com"
sender_password = "lzrfuvdimoerhlkr "  # See note below about app passwords
recipient_email = "adityako@bu.edu"
subject = "Test HTML Email"
       

# --- Updated HTML Template with new placeholders ---
base_html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Transactional Email</title>
  <style type="text/css">
  img{{
    width:100%;
    max-width:640px;
  }}
    /* MOBILE STYLES */
    @media only screen and (max-width: 640px) {{
      .wrapper {{
        width: 100% !important;
        max-width: 100% !important;
      }}
      .mobile-img {{
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
      }}
      .mobile-padding {{
        padding: 10px !important;
      }}
    }}
    table{{
        background-color:#fff;
    }}
     /* Table Styles for HTML Email */
    table.dataframe {{
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 1em; /* Add some space below the table */
        font-family: Helvetica, sans-serif; /* Ensure font consistency */
    }}
    table.dataframe th,
    table.dataframe td {{
        border: 1px solid #ddd; /* Light grey border */
        padding: 8px; /* Cell padding */
        text-align: left; /* Align text left */
        font-size: 11pt; /* Set font size */
    }}
    table.dataframe th {{
        background-color: #f2f2f2; /* Light grey background for headers */
        color: #333; /* Darker text color for headers */
        font-weight: bold; /* Bold headers */
    }}
     table.dataframe tr:nth-child(even) {{
        background-color: #f9f9f9; /* Zebra striping for rows */
    }}
  </style>
</head>

<body style="margin:0; padding:0; background-color:#f4f5f6; font-family:Helvetica, sans-serif;">

  <!-- OUTER TABLE (100% WIDTH) -->
  <table
    width="100%"
    border="0"
    cellpadding="0"
    cellspacing="0"
    bgcolor="#f4f5f6"
    style="background-color:#f4f5f6;"
  >
    <tr>
      <td align="center" style="padding:20px 10px;">

        <!-- INNER WRAPPER (max-width:640px) -->
        <table
          class="wrapper"
          width="100%"
          border="0"
          cellpadding="0"
          cellspacing="0"
          style="max-width:640px; margin:0 auto; background-color:#ffffff;"
        >

          <!-- LOGO ROW -->
          <tr>
            <td align="center" class="mobile-padding" style="padding:20px 0; border-bottom:2px solid #660099;">
              <img
                src="https://news.bostonscientific.com/file.php/201084/BSC_wtag_541blue_rgb-large+update+1.png"
                alt="Company Logo"
                width="150"
                style="display:block; width:100%; max-width:150px; height:auto;"
              >
            </td>
          </tr>

          <!-- BANNER IMAGE ROW -->
          <tr>
            <td align="center" style="padding:0;">
              <img
                class="mobile-img"
                src="https://cdn.brandfetch.io/idReCDTTz1/w/1500/h/500/id0YqjToGb.jpeg?c=1dxbfHSJFAPEGdCLU4o5B"
                alt="Banner Image"
                width="640"
                style="display:block; width:100%; max-width:640px; height:auto; margin-bottom: 16px;"
              >
            </td>
          </tr>
          <!--OVERVIEW OF KEY METRICS AND STUDY HIGHLIGHTS-->
          <tr>
            <td align="center" style="padding: 0; border-bottom:2px solid #660099;">
                <h1 style="text-align:left; padding-left: 16px;">Overview of Key Metrics and Study Highlights</h1>
                <table
                width="100%"
                border="0"
                cellpadding="0"
                cellspacing="0"
                style="box-sizing: border-box; max-width:640px; margin:0 auto; background-color:#ffffff;padding: 16px;">
                    <td>
                        {section_1}
                    </td>
                </table>
            </td>
          </tr>

          <!-- IMAGE BETWEEN SECTIONS 1 and 2 -->
          <tr>
            <td align="center" style="padding:0;">
              <img
                class="mobile-img"
                src="https://www.bostonscientific.com/en-US/about-us/core-businesses/endoscopy/_jcr_content/root/container/container_469576080/teaser_copy.coreimg.90.1600.jpeg/1711028390316/endoscopy-hero-banner-new.jpeg"
                alt="Banner Image"
                width="640"
                style="display:block; width:100%; max-width:640px; height:auto; margin-bottom: 16px;"
              >
            </td>
          </tr>

          <!-- UPCOMING PROJECTS AND TIMELINES -->
          <tr>
            <td align="center" style="padding: 0; border-bottom:2px solid #660099;">
                <h1 style="text-align:left; padding-left: 16px;">Upcoming Projects and Timelines</h1>
                <table
                width="100%"
                border="0"
                cellpadding="0"
                cellspacing="0"
                style="box-sizing: border-box; max-width:640px; margin:0 auto; background-color:#ffffff;padding: 16px;">
                    <td>
                        {section_2} 
                    </td>
                </table>
            </td>
            </tr>

            <!-- IMAGE BETWEEN SECTIONS 2 and 3 -->
            <tr>
            <td align="center" style="padding:0;">
              <img
                class="mobile-img"
                src="https://www.bostonscientific.com/en-US/about-us/core-businesses/_jcr_content/root/container/container_469576080/teaser_copy.coreimg.90.1600.jpeg/1711689429537/business-homepage-hero-banner-new.jpeg"
                alt="Banner Image"
                width="640"
                style="display:block; width:100%; max-width:640px; height:auto; margin-bottom: 16px;"
              >
            </td>
            </tr>

            <!-- CALLS TO ACTION -->
            <tr>
            <td align="center" style="padding: 0; border-bottom:2px solid #660099;">
                <h1 style="text-align:left; padding-left: 16px;">Calls to Action</h1>
                <table
                width="100%"
                border="0"
                cellpadding="0"
                cellspacing="0"
                style="box-sizing: border-box; max-width:640px; margin:0 auto; background-color:#ffffff;padding: 16px;">
                    <td>
                        {section_3}
                    </td>
                </table>
            </td>
            </tr>

            <!-- IMAGE BETWEEN SECTIONS 3 and 4 -->
            <tr>
            <td align="center" style="padding:0;">
              <img
                class="mobile-img"
                src="https://www.bostonscientific.com/en-US/about-us/core-businesses/electrophysiology/_jcr_content/root/container/container_469576080/teaser_copy.coreimg.90.1600.jpeg/1716464235086/ep-business-hero-banner-new.jpeg"
                alt="Banner Image"
                width="640"
                style="display:block; width:100%; max-width:640px; height:auto; margin-bottom: 16px;"
              >
            </td>
            </tr>

            <!-- REVIEW OF CROSS-FUNCTIONAL COLLABORATIONS -->
            <tr>
            <td align="center" style="padding: 0; border-bottom:2px solid #660099;">
                <h1 style="text-align:left; padding-left: 16px;">Review of Cross-Functional Collaborations</h1>
                <table
                width="100%"
                border="0"
                cellpadding="0"
                cellspacing="0"
                style="box-sizing: border-box; max-width:640px; margin:0 auto; background-color:#ffffff;padding: 16px;">
                    <td>
                        {section_4} 
                    </td>
                </table>
            </td>
            </tr>
             <!-- IMAGE AFTER SECTION 4 (Optional, keeping the pattern) -->
            <tr>
            <td class="content-padding footer-text" style="padding:20px;text-align:center;font-size:12px;color:#999999;border-top:1px solid #dddddd;">
              bsc@bsc.com
              © 2025 Boston Scientific. All rights reserved.
            </td>
            </tr>


          <!-- ADDITIONAL CONTENT ROWS HERE -->
          <!-- <tr>…</tr> -->

        </table>
        <!-- END INNER WRAPPER -->

      </td>
    </tr>
    
  </table>
  <!-- END OUTER TABLE -->

</body>
</html>


"""

def send_html_email(sender_email, sender_password, recipient_email, subject, html_content):
    # Create message container
    print("function_called")
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    
    # Create the HTML part of the message
    html_part = MIMEText(html_content, 'html')
    
    # Attach HTML to the email
    message.attach(html_part)
    
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    try:
        # Login to your Gmail account
        server.login(sender_email, sender_password)
        
        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        # Close the connection
        server.quit()

# --- Streamlit App Setup ---
st.set_page_config(page_title="Email Template Generator", layout="wide")
st.title("APAC RWE Update Email Generator")
st.markdown("Generate a responsive HTML email based on the provided template structure.")
st.subheader("General instructions")
st.markdown("The template has 4 pre-determined sections")
st.markdown("- Overview of Key Metrics and Study Highlights")
st.markdown("- Upcoming Projects and Timelines")
st.markdown("- Calls to Action")
st.markdown("- Review of Cross-Functional Collaborations")
st.markdown("You may add sub-sections/items for each of these sections using the button found directly under these sections headings (e.g 'Add Metric/Highlight item' button)")
st.markdown("When the  respective button is clicked you get an input field to add a heading, with a text editor underneath it to add the content of that sub-sections, you also get the option to add a table to the end of that subsection by uploading a csv to the file upload option underneath the text editor")
st.markdown("The text editor allows you to format the content the way you see fit, you may also add links to the text if you wish to do so")
st.markdown("Once you have added content for each section, you must click on the 'Generate Email Template' button found at the end, to create the email, it will also open a preview section to view how the email would look like")
st.markdown("Once you clicked the 'Generate Email Template' button and confirm that the email is correctly created, you can then enter the recepient of the test email in the respective input field and click the 'send test email' button, this will send the content generated to the email of your choice (please note that you may find the email in your spam folder from the email 'aditya.tempbs@gmail.com') ")
st.markdown("Alternatively you can also download the html content of the template by clicking on the respective button if you wish to do so")

# --- Initialize Session State for Sections ---
if 'sec1' not in st.session_state:
    st.session_state.sec1 = {} # Overview of Key Metrics
if 'sec2' not in st.session_state:
    st.session_state.sec2 = {} # Upcoming Projects
if 'sec3' not in st.session_state:
    st.session_state.sec3 = {} # Calls to Action
if 'sec4' not in st.session_state:
    st.session_state.sec4 = {} # Cross-Functional Collaborations

# --- Helper Function to add rows to specific sections ---
def add_row_to_section(section_key):
    """Adds a new entry key to the specified section in session state."""
    current_section = st.session_state[section_key]
    idx = len(current_section)
    # Use a unique key like 'sec1_sub_0', 'sec2_sub_0' etc.
    new_key = f"{section_key}_sub_{idx}"
    current_section[new_key] = {} # Initialize with an empty dict if needed
    # Initialize specific keys if they are always expected, e.g., table
    # if f'table_{new_key}' not in st.session_state:
    #     st.session_state[f'table_{new_key}'] = None
    return new_key # Return the key in case we need it

# --- Input Section 1: Overview of Key Metrics and Study Highlights ---
st.subheader("Overview of Key Metrics and Study Highlights")
if st.button("Add Metric/Highlight Item", key="add_sec1_item"):
    add_row_to_section('sec1')

sec1_data_list = [] # List to store collected data for HTML generation
for idx, key in enumerate(st.session_state.sec1):
    st.markdown(f"--- **Item {idx+1}** ---")
    # Using unique keys based on section and loop key
    heading = st.text_input(f"Metric/Highlight Heading", key=f"sec1_heading_{key}")
    summary = st_quill(html=st.session_state.get(f"sec1_summary_{key}", ""), key=f"sec1_summary_{key}") # Use get for initial empty
    uploaded_file = st.file_uploader("Upload CSV to be included (Optional)", accept_multiple_files=False, key=f"sec1_file_upload_{key}" )

    df = None
    table_html = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.index+=1
            # Assuming the first column is index-like, remove it if necessary
            # df = df.iloc[:, 1:]
            # df.index += 1 # Add 1 to index if needed for display

            # Generate HTML table with inline styles
            styles = [
                {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%'), ('margin-bottom', '1em'), ('margin-top', '1em'), ('font-family', 'Helvetica, sans-serif')]},
                {'selector': 'th, td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'left'), ('font-size', '11pt')]},
                {'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('color', '#333'), ('font-weight', 'bold')]},
                {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
            ]

            table_html = (
                df.style
                .set_table_styles(styles)
                .set_table_attributes('class="dataframe"')
                .to_html()
            )
            st.dataframe(df, hide_index=True) # Display for user
            st.session_state[f'sec1_table_html_{key}'] = table_html # Store HTML for later

        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            st.session_state[f'sec1_table_html_{key}'] = None # Clear if error
    else:
         st.session_state[f'sec1_table_html_{key}'] = None # Clear if file is removed

    # Collect data for HTML generation
    sec1_item_data = {'heading': heading, 'summary': summary}
    if st.session_state.get(f'sec1_table_html_{key}') is not None:
        sec1_item_data['table_html'] = st.session_state[f'sec1_table_html_{key}']
    sec1_data_list.append(sec1_item_data)


# --- Input Section 2: Upcoming Projects and Timelines ---
st.subheader("Upcoming Projects and Timelines")
if st.button("Add Project/Timeline Item", key="add_sec2_item"):
    add_row_to_section('sec2')

sec2_data_list = []
for idx, key in enumerate(st.session_state.sec2):
    st.markdown(f"--- **Item {idx+1}** ---")
    heading = st.text_input(f"Project/Timeline Heading", key=f"sec2_heading_{key}")
    summary = st_quill(html=st.session_state.get(f"sec2_summary_{key}", ""), key=f"sec2_summary_{key}")
    uploaded_file = st.file_uploader("Upload CSV for Details (Optional)", accept_multiple_files=False, key=f"sec2_file_upload_{key}" )

    df = None
    table_html = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.index+=1
             # Generate HTML table with inline styles
            styles = [
                {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%'), ('margin-bottom', '1em'), ('margin-top', '1em'), ('font-family', 'Helvetica, sans-serif')]},
                {'selector': 'th, td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'left'), ('font-size', '11pt')]},
                {'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('color', '#333'), ('font-weight', 'bold')]},
                {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
            ]
            table_html = (
                df.style
                .set_table_styles(styles)
                .set_table_attributes('class="dataframe"')
                .to_html()
            )
            st.dataframe(df, hide_index=True)
            st.session_state[f'sec2_table_html_{key}'] = table_html
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            st.session_state[f'sec2_table_html_{key}'] = None
    else:
         st.session_state[f'sec2_table_html_{key}'] = None

    sec2_item_data = {'heading': heading, 'summary': summary}
    if st.session_state.get(f'sec2_table_html_{key}') is not None:
         sec2_item_data['table_html'] = st.session_state[f'sec2_table_html_{key}']
    sec2_data_list.append(sec2_item_data)


# --- Input Section 3: Calls to Action ---
st.subheader("Calls to Action")
st.markdown("Suggest specific actions or areas where collaboration is needed.")
if st.button("Add Call to Action", key="add_sec3_item"):
    add_row_to_section('sec3')

sec3_data_list = []
for idx, key in enumerate(st.session_state.sec3):
    st.markdown(f"--- **Item {idx+1}** ---")
    heading = st.text_input(f"Action item heading", key=f"sec3_heading_{key}")
    summary = st_quill(html=st.session_state.get(f"sec3_summary_{key}", ""), key=f"sec3_summary_{key}")
    uploaded_file = st.file_uploader("Upload CSV for Results/Details (Optional)", accept_multiple_files=False, key=f"sec3_file_upload_{key}" )

    df = None
    table_html = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.index+=1
            # Generate HTML table with inline styles
            styles = [
                {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%'), ('margin-bottom', '1em'), ('margin-top', '1em'), ('font-family', 'Helvetica, sans-serif')]},
                {'selector': 'th, td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'left'), ('font-size', '11pt')]},
                {'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('color', '#333'), ('font-weight', 'bold')]},
                {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
            ]
            table_html = (
                df.style
                .set_table_styles(styles)
                .set_table_attributes('class="dataframe"')
                .to_html()
            )
            st.dataframe(df, hide_index=True)
            st.session_state[f'sec3_table_html_{key}'] = table_html
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            st.session_state[f'sec3_table_html_{key}'] = None
    else:
         st.session_state[f'sec3_table_html_{key}'] = None

    sec3_item_data = {'heading': heading, 'summary': summary}
    if st.session_state.get(f'sec3_table_html_{key}') is not None:
         sec3_item_data['table_html'] = st.session_state[f'sec3_table_html_{key}']
    sec3_data_list.append(sec3_item_data)


# --- Input Section 4: Review of Cross-Functional Collaborations ---
st.subheader("Review of Cross-Functional Collaborations")
st.markdown("Highlight successful collaborations and available resources.")
if st.button("Add Collaboration Highlight", key="add_sec4_item"):
    add_row_to_section('sec4')

sec4_data_list = []
for idx, key in enumerate(st.session_state.sec4):
    st.markdown(f"--- **Item {idx+1}** ---")
    heading = st.text_input(f"Collaboration/Resource Highlight Heading", key=f"sec4_heading_{key}")
    summary = st_quill(html=st.session_state.get(f"sec4_summary_{key}", ""), key=f"sec4_summary_{key}")
    uploaded_file = st.file_uploader("Upload CSV for Results/Details (Optional)", accept_multiple_files=False, key=f"sec4_file_upload_{key}" )

    df = None
    table_html = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.index+=1
            # Generate HTML table with inline styles
            styles = [
                {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%'), ('margin-bottom', '1em'), ('margin-top', '16px'), ('font-family', 'Helvetica, sans-serif')]},
                {'selector': 'th, td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'left'), ('font-size', '11pt')]},
                {'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('color', '#333'), ('font-weight', 'bold')]},
                {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
            ]
            table_html = (
                df.style
                .set_table_styles(styles)
                .set_table_attributes('class="dataframe"')
                .to_html()
            )
            st.dataframe(df, hide_index=True)
            st.session_state[f'sec4_table_html_{key}'] = table_html
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            st.session_state[f'sec4_table_html_{key}'] = None
    else:
         st.session_state[f'sec4_table_html_{key}'] = None

    sec4_item_data = {'heading': heading, 'summary': summary}
    if st.session_state.get(f'sec4_table_html_{key}') is not None:
         sec4_item_data['table_html'] = st.session_state[f'sec4_table_html_{key}']
    sec4_data_list.append(sec4_item_data)


# --- HTML Generation Functions ---
def create_section_content(data_list):
    """Generic function to create HTML content for a section."""
    section_html = ""
    for item in data_list:
        heading = f"<h2>{item.get('heading', '')}</h2>" if item.get('heading') else ""
        content = item.get("summary", "")
        table = item.get("table_html", "")
        if table!="":
            section_html += heading + content + table +"<br>"
        else:
            section_html += heading + content + table
    return section_html

# --- Generate Button ---
if st.button("Generate Email Template"):
    # Generate HTML content for each section
    section_1_html = create_section_content(sec1_data_list)
    section_2_html = create_section_content(sec2_data_list)
    section_3_html = create_section_content(sec3_data_list) # Section 3 has no table option in the UI, but the function handles it
    section_4_html = create_section_content(sec4_data_list)

    # Format the base HTML template with the generated section contents
    generated_html = base_html.format(
        section_1=section_1_html,
        section_2=section_2_html,
        section_3=section_3_html,
        section_4=section_4_html
    )
    st.session_state['generated_html'] = generated_html
    # Display the generated HTML
    st.subheader("Generated HTML Email Preview")
    

    # Optional: Add a download button for the HTML
    st.download_button(
        label="Download HTML",
        data=generated_html,
        file_name="apac_rwe_update.html",
        mime="text/html"
    )

if 'generated_html' in st.session_state:
        components.html(st.session_state.generated_html, height=800, scrolling=True, width=None)

if "recipient_email" not in st.session_state:
    st.session_state.recipient_email = ""

st.session_state.recipient_email = st.text_input("send test email to:")



if st.session_state.recipient_email!="":
    if 'generated_html' in st.session_state:
        if st.button("send test email"):
                try:
                    if 'generated_html' in st.session_state:
                        print("button_press")
                        send_html_email(sender_email, sender_password, recipient_email, subject, st.session_state.generated_html)
                        st.warning('email sent!', icon="👌")
                    else:
                        print("no_html")
                except:
                    st.warning('a problem occured', icon="⚠️")
    else:
        st.warning('generate valid email template', icon="⚠️")
else:
    st.warning('enter email', icon="⚠️")
