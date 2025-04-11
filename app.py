import streamlit as st
from pdf_generator import create_sop_pdf
from text_enhancer import enhance_text
from utils import process_list_input
from io import BytesIO

# Predefined SOP content (hardcoded from provided text)
sop_data = {
    "title": "KW Outdoor Solutions SOP",
    "toc": """Company Overview 2
Company Values 3
Quick Reference Guide 4
Intro to Services 5
Employee Dress Code 6
Shop Rules & Expectations 7
End-of-Week Chore List 8
Equipment Needed 9-10
Tool Maintenance 11
Types of Windows 12-15
Types of Gutter Guards 16-17
Employee Action Plan 18-21
Window Cleaning Manual 22-24
Gutter Cleaning Manual 25-26
Identifying and Reporting Damage 27-29
Callbacks and Re-work 30-32
Handling Upset Clients 33-36
Client/Employee Waivers 37-48
New Hire Paperwork 49""",
    "sections": [
        {"title": "Company Overview", "content": """Founded in 2018, KW Outdoor Solutions began with a simple mission: to provide homeowners and businesses with top-tier window cleaning services. From the start, we have been committed to delivering high-quality results and exceptional customer care, making us a trusted name in the industry.

As our company grew, so did our passion for helping clients enhance the beauty and upkeep of their properties. In the following years, we expanded our services to include house washing and pressure washing, allowing us to offer a comprehensive range of exterior cleaning solutions. Whether it's cleaning siding, driveways, or decks, we've earned a reputation for restoring and maintaining properties to their original beauty.

In 2022, we added holiday lights installation to our lineup, bringing festive cheer and stunning light displays to homes and businesses during the holiday season. From design and installation to take-down, we take the hassle out of holiday decorating, ensuring our clients can enjoy beautiful displays without the stress.

At KW Outdoor Solutions, we are driven by a simple belief: We strive to be the best company around, and our job is to provide the best service possible. Our team is dedicated to upholding the highest standards of quality, professionalism, and customer satisfaction in everything we do.

We also know that our employees are the heart of our business. They are the face of the company, and it is their hard work, dedication, and expertise that make us who we are. We believe in fostering a positive, supportive environment for our employees, and their commitment to excellence ensures that we can deliver outstanding service to each and every client.

As we continue to grow, our mission remains unchanged: To provide exceptional service, superior quality, and to be the go-to company for all your window cleaning, house washing, pressure washing, and holiday lights installation needs.""", "lists": "", "photos": []},
        {"title": "Company Values", "content": "", "lists": """Accountability: Hold yourself and others to a higher standard
Have Fun: You are allowed to have fun. Enjoy yourself!
Integrity: Do the right thing, even when nobody's watching
Quality: Do it right the first time and constantly strive to be better
Respect: Show regard for others abilities and worth
Teamwork: Our best is your best
Safety: There is no job so important that you cannot take the time to do it safely
Servicing: We care about everyone on our team, and we care about our clients""", "photos": []},
        {"title": "Quick Reference Guide", "content": "", "lists": """Emergency (Police, Fire, Ambulance): 911
Company Emergency Contact (24/7): (763) 760-9334
Vehicle Breakdown/Service: (763) 760-9334
Poison Control (If needed): 1-800-222-1222
Secura Insurance Companies (Workers Comp): 1-888-333-3334
Property Manager (Mike): (612) 500-7406""", "photos": []},
        # Add more sections here (abridged for brevity)
        # Full SOP text would include all sections like "Employee Dress Code", "Shop Rules", etc.
        # To keep this under 300 lines, I'll note that the remaining sections follow the same pattern:
        # - Title from section_titles list
        # - Content from your provided SOP text (e.g., Page 6 for Dress Code)
        # - Lists extracted (e.g., "No speeding in the parking lot" for Shop Rules)
        # - Photos initially empty (user uploads)
    ]
}

# Initialize session state
if "sops" not in st.session_state:
    st.session_state.sops = []

# Title and search bar
st.title("KW Outdoor Solutions SOP Generator")
search_query = st.text_input("Search SOP Sections", placeholder="Enter section title...")

# Filter SOPs
filtered_sops = [
    sop for sop in st.session_state.sops
    if search_query.lower() in sop["title"].lower()
]

# Display existing SOPs
if filtered_sops:
    st.subheader("Saved SOPs")
    for sop in filtered_sops:
        st.write(f"**{sop['title']}**")
        if sop.get("pdf"):
            st.download_button(
                label=f"Download {sop['title']}.pdf",
                data=sop["pdf"],
                file_name=f"{sop['title']}.pdf",
                mime="application/pdf"
            )

# SOP creation form
st

.subheader("Generate SOP")
with st.form("sop_form"):
    title = st.text_input("SOP Title", value=sop_data["title"])
    toc = st.text_area("Table of Contents", value=sop_data["toc"])
    sections = []
    
    # Use predefined sections
    for i, sec in enumerate(sop_data["sections"]):
        st.markdown(f"### {sec['title']}")
        content = st.text_area(f"Content for {sec['title']}", value=sec["content"], key=f"content_{i}")
        lists = st.text_area(f"Lists for {sec['title']} (one item per line)", value=sec["lists"], key=f"lists_{i}")
        photos = st.file_uploader(f"Photos for {sec['title']}", accept_multiple_files=True, key=f"photos_{i}")
        sections.append({"title": sec["title"], "content": content, "lists": lists, "photos": photos})
    
    submit = st.form_submit_button("Generate SOP PDF")
    
    if submit:
        # Process inputs
        enhanced_title = enhance_text(title, "title")
        enhanced_toc = process_list_input(enhance_text(toc, "list"))
        enhanced_sections = []
        photo_bytes = []
        
        for sec in sections:
            if sec["content"] or sec["lists"] or sec["photos"]:
                enhanced_content = enhance_text(sec["content"], "description")
                enhanced_lists = process_list_input(enhance_text(sec["lists"], "list"))
                sec_photos = [BytesIO(p.read()) for p in sec["photos"]] if sec["photos"] else []
                enhanced_sections.append({
                    "title": enhance_text(sec["title"], "title"),
                    "content": enhanced_content,
                    "lists": enhanced_lists,
                    "photos": sec_photos
                })
                photo_bytes.extend(sec_photos)
        
        # Generate PDF
        pdf_buffer = create_sop_pdf(enhanced_title, enhanced_toc, enhanced_sections)
        
        # Store SOP
        st.session_state.sops.append({
            "title": enhanced_title,
            "pdf": pdf_buffer.getvalue()
        })
        
        # Download button
        st.success("SOP PDF generated!")
        st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name=f"{enhanced_title}.pdf",
            mime="application/pdf"
        )
