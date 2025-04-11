import streamlit as st
from pdf_generator import create_sop_pdf
from text_enhancer import enhance_text
from utils import process_list_input
from io import BytesIO

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
st.subheader("Create SOP")
with st.form("sop_form"):
    title = st.text_input("SOP Title", value="KW Outdoor Solutions SOP")
    toc = st.text_area("Table of Contents", placeholder="Enter sections and page numbers (one per line)")
    sections = []
    
    # Predefined sections to match SOP
    section_titles = [
        "Company Overview", "Company Values", "Quick Reference Guide", "Intro to Services",
        "Employee Dress Code", "Shop Rules & Expectations", "End-of-Week Chore List",
        "Equipment Needed", "Tool Maintenance", "Types of Windows", "Types of Gutter Guards",
        "Employee Action Plan", "Window Cleaning Manual", "Gutter Cleaning Manual",
        "Identifying and Reporting Damage", "Callbacks and Re-work", "Handling Upset Clients",
        "Client/Employee Waivers", "New Hire Paperwork"
    ]
    
    for i, sec_title in enumerate(section_titles):
        st.markdown(f"### {sec_title}")
        content = st.text_area(f"Content for {sec_title}", key=f"content_{i}")
        lists = st.text_area(f"Lists for {sec_title} (one item per line)", key=f"lists_{i}")
        photos = st.file_uploader(f"Photos for {sec_title}", accept_multiple_files=True, key=f"photos_{i}")
        sections.append({"title": sec_title, "content": content, "lists": lists, "photos": photos})
    
    submit = st.form_submit_button("Generate SOP PDF")
    
    if submit and title and toc:
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
