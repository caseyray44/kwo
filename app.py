import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from io import BytesIO

# Hardcoded SOP content, page by page
sop_pages = [
    # Page 1: Table of Contents
    {
        "title": "Table of Contents",
        "content": """Company Overview 2
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
New Hire Paperwork 49"""
    },
    # Page 2: Company Overview
    {
        "title": "Company Overview",
        "content": """Founded in 2018, KW Outdoor Solutions began with a simple mission: to provide homeowners and businesses with top-tier window cleaning services. From the start, we have been committed to delivering high-quality results and exceptional customer care, making us a trusted name in the industry.

As our company grew, so did our passion for helping clients enhance the beauty and upkeep of their properties. In the following years, we expanded our services to include house washing and pressure washing, allowing us to offer a comprehensive range of exterior cleaning solutions. Whether it's cleaning siding, driveways, or decks, we've earned a reputation for restoring and maintaining properties to their original beauty.

In 2022, we added holiday lights installation to our lineup, bringing festive cheer and stunning light displays to homes and businesses during the holiday season. From design and installation to take-down, we take the hassle out of holiday decorating, ensuring our clients can enjoy beautiful displays without the stress.

At KW Outdoor Solutions, we are driven by a simple belief: We strive to be the best company around, and our job is to provide the best service possible. Our team is dedicated to upholding the highest standards of quality, professionalism, and customer satisfaction in everything we do.

We also know that our employees are the heart of our business. They are the face of the company, and it is their hard work, dedication, and expertise that make us who we are. We believe in fostering a positive, supportive environment for our employees, and their commitment to excellence ensures that we can deliver outstanding service to each and every client.

As we continue to grow, our mission remains unchanged: To provide exceptional service, superior quality, and to be the go-to company for all your window cleaning, house washing, pressure washing, and holiday lights installation needs."""
    },
    # Page 3: Company Values
    {
        "title": "Company Values",
        "content": """Accountability

Hold yourself and others to a higher standard

Have Fun

You are allowed to have fun. Enjoy yourself!

Integrity

Do the right thing, even when nobody's watching

Quality

Do it right the first time and constantly strive to be better

Respect

Show regard for others abilities and worth

Teamwork

Our best is your best

Safety

There is no job so important that you cannot take the time to do it safely

Servicing

We care about everyone on our team, and we care about our clients"""
    },
    # Page 4: Quick Reference Guide
    {
        "title": "Quick Reference Guide",
        "content": """Emergency Contacts

- Emergency (Police, Fire, Ambulance): 911
- Company Emergency Contact (24/7): (763) 760-9334
- Vehicle Breakdown/Service: (763) 760-9334
- Poison Control (If needed): 1-800-222-1222
- Secura Insurance Companies (Workers Comp): 1-888-333-3334
- Property Manager (Mike): (612) 500-7406"""
    },
    # Page 5: Intro to Services
    {
        "title": "Introduction to Services",
        "content": """This section is an introduction to our window cleaning and gutter cleaning services. It explains and elaborates why these services are important to our clients and maintaining their properties.

Professional Window Cleaning

- Enhances Curb Appeal/Increases Property Value: Clients may have their windows cleaned prior to selling their property.
- Prolongs Window Life/Prevents Damage: Regular cleaning helps protect your windows from the buildup of dirt, dust, hard water stains, and other corrosive materials that can cause scratches and damage over time.
- Improves Indoor Air Quality: Prevents dust, pollen and other allergens from collecting on the outside of the window that can seep inside once the window is opened.
- Better Light and Views: Clean windows allow more natural light into your space.

Professional Gutter Cleaning

- Prevents Water Damage/Ice Dams: Clean gutters direct water away from the foundation of the property and prevents ice build up in cold weather that can cause leaks inside the property.
- Protects the Roof and Siding: Clogged gutters can cause water to back up under roof shingles, leading to leaks, rot, and mold growth.
- Prevents Pest Infestations: Stagnant water in clogged gutters can attract pests like mosquitoes, termites, and rodents."""
    },
    # Page 6: Employee Dress Code
    {
        "title": "Employee Dress Code",
        "content": """At KW Outdoor Solutions, we take pride in maintaining a professional and cohesive appearance while on the job. To ensure consistency and safety, all employees are required to adhere to the following dress code guidelines:

Company-Issued Apparel:

- Employees will be provided company-issued t-shirts, sweatshirt, shorts, and hat/beanie while on duty.
- These items should be clean and in good condition at all times.
- Alterations (i.e. cutting of sleeves or cropping) are not allowed.
- New company-issued apparel will be issued as needed from general wear and tear. If an employee loses an item, it is the employee's responsibility to purchase new apparel.

General Appearance:

- Clothing should be clean and presentable at the start of each shift.
- Personal hygiene must be maintained to ensure a professional representation of the company.
- Employees should dress appropriately for the weather while still adhering to the dress code.
- All bottoms must fit appropriately-overly baggy or excessively tight clothing is not permitted.

Shoes:

- No open-toed shoes are permitted while working.
- Shoes must not have significant damage to them (i.e. large holes or cracks) and odor must remain minimal. Remember, we are guests in peoples homes.

Cost of Apparel

- Shirts: $25
- Short: $15
- Sweatshirt: $65
- Hat: $25
- Beanie: $20

If you have any questions or require additional uniform items, please contact your supervisor."""
    },
    # Page 7: Shop Rules & Expectations
    {
        "title": "Shop Rules & Expectations",
        "content": """Maintaining a clean, safe, and organized workspace is essential to ensuring efficiency and professionalism. All employees are expected to adhere to the following shop rules and expectations:

1. Parking & Safety:

- No speeding in the parking lot. Drive cautiously at all times.
- Employee vehicles must be parked in designated areas only.
- Company vehicles must not block other unit entrances or driveways when parked outside of the shop.

2. Shop Security & Organization:

- Ensure all shop doors are securely closed upon leaving.
- All equipment must be stored and returned to its original spot after use.
- Vehicles must be parked in their designated spots inside the shop.

3. Cleanliness & Maintenance:

- Floors must be swept on a weekly basis to maintain a clean work environment.
- The refrigerator must remain clean. Employees are responsible for removing expired or unwanted items.
- The bathroom must remain clean; please notify management of any issues.
- Garbage is emptied on Fridays.
- Leaf blower batteries must be placed on the charger at the end of each workday.
- All items are to be returned to shelves or hangers after use.

4. Employee Spaces & Personal Responsibility:

- Lockers must remain organized and free of unnecessary clutter.
- The coat and shoe area should always be presentable and tidy.
- Used towels must be placed in the designated dirty bin at the end of each workday.
- Company vehicles must remain clean and free of garbage at all times.

By following these rules, we can ensure a safe, organized, and professional work environment for everyone. Failure to adhere to these expectations may result in corrective action. Thank you for your cooperation and commitment to maintaining our workplace standards!"""
    },
    # Page 8: End-of-Week Chore List
    {
        "title": "End-of-Week Employee Checklist",
        "content": """To maintain a clean and organized workspace, all employees are expected to complete the following tasks by the end of each work week:

Sweep the Shop - Ensure all floors are free of dirt and debris.

Clean Vehicles

- Remove dirty towels and place them in the designated bins.
- Take out all garbage from vehicles.
- Vacuum interior floors, back of van, and seats as needed.
- Thoroughly wipe down all surfaces, including dashboards, consoles, and door panels.
- Restock necessary supplies (steel wool, soaps, etc.).
- Replace clean towels for next use.

Wipe Down Counters - Clean and sanitize all shop counters and work surfaces.

Organize Personal Space - Ensure lockers, coat and shoe areas, and personal storage spaces are tidy.

Empty & Clean the Fridge - Remove expired or leftover food, wipe down shelves, and ensure the fridge is clean and odor-free.

Take Out Trash - Empty all garbage cans as needed and replace liners.

Return Supplies - Put all unnecessary tools and supplies back in their designated places on shelves or hooks.

Failure to complete these tasks may result in disciplinary action. All employees are responsible for maintaining a clean and professional workspace."""
    },
    # Page 9: Equipment Needed (Window Cleaning)
    {
        "title": "Window Cleaning Equipment",
        "content": """Tool Belt: $50

Large Wet Wand: $25

Squeegees

18": $55, 14": $50, 6": $20

Salt Bucket: $25

Small Wet Wand: $20

Scrubber Pad: $25

Water Bucket: $25"""
    },
    # Page 10: Equipment Needed (Continued)
    {
        "title": "Window Cleaning Equipment (Continued)",
        "content": """Soap Bottle

Steel Wool

5-in-1 Tool

Soap

Window Scrapers

Track Cleaning Tools"""
    },
    # Page 11: Gutter Cleaning Equipment
    {
        "title": "Gutter Cleaning Equipment",
        "content": """Gutter Hawg

Hose

Sprayer Nozzle

Leaf Blower

Rake

Yard Waste Bags"""
    },
    # Page 12: Tool Maintenance
    {
        "title": "Tool Maintenance",
        "content": """Window Cleaning Tools

Tool Belt:

- Empty all rusty steel wool from toolbelt daily
- If toolbelt is damp/wet, hang to dry

Belt Bucket:

- Empty excess water from belt bucket after each use

Wet Wand:

- Rinse out wet wand daily to remove any dirt particles
- Change wet wand sleeve weekly to be washed

Squeegee:

- Change squeegee blades weekly
- Avoid dropping squeegees, as they bend easily and create problems with squeegee

Scrubber Pad:

- Replace walnut pad as it becomes worn down

Water Bucket:

- Empty water bucket after each job (rinse out mud or other debris)
- DO NOT PUT WATER BUCKET IN VAN WTH WATER IN IT

Window Scraper:

- Replace rusty or chipped blades immediately
- Replace every few days to weekly

Gutter Cleaning Tools

Gutter Hawg:

- Avoid dropping as plastic is not that durable

Leaf Blower:

- Put batteries on charger after each use
- DO NOT DROP

Hose:

- Drain water after each use before putting in van"""
    },
    # Page 13: Types of Windows (Part 1)
    {
        "title": "Types of Windows",
        "content": """There are several types of windows, each with different designs, functions, and aesthetic appeal. Below are some of the most common types of windows:

1. Double-Hung Windows

- Both sashes move up and down for easier cleaning.
- Found in many traditional/new homes.

BOTH SASHES OPEN

2. Casement/Crank-out Windows

- Hinged on the side and open outward with a crank.
- Common in modern and energy-efficient homes."""
    },
    # Page 14: Types of Windows (Part 2)
    {
        "title": "Types of Windows (Continued)",
        "content": """3. Sliding Windows/Doors

- Open horizontally by sliding one panel over the other.
- Often seen in contemporary homes and apartments.

4. Awning Windows

- Hinged at the top and open outward, allowing ventilation even during rain.
- Often found in bathrooms or basements.

5. Picture Windows

- Large, fixed windows that do not open.
- Provide unobstructed views but require special cleaning due to their size."""
    },
    # Page 15: Types of Windows (Part 3)
    {
        "title": "Types of Windows (Continued)",
        "content": """6. Bay & Bow Windows

- Bay: Three panels extending outward, usually with a larger center pane.
- Bow: A curved set of four or more panels.
- Often seen in living rooms or dining areas.

Bay Window

Bow Window

7. Skylight Windows

- Installed on the roof for natural light.
- Can be fixed or operable for ventilation.

8. Storm Windows

- Installed over existing windows for extra insulation.
- Common in older homes and areas with extreme weather."""
    },
    # Page 16: Types of Windows (Part 4)
    {
        "title": "Types of Windows (Continued)",
        "content": """9. Storm Doors

- Usually on the outside of a main door
- Provides protection from the elements

10. French Door/Window

- Small individual panes of glass within a large window.
- Panes are separated by a grille/grid"""
    },
    # Page 17: Types of Gutter Guards (Part 1)
    {
        "title": "Types of Gutter Guards",
        "content": """Gutter guards are designed to keep debris out of your gutters, to help reduce clogging and make gutter maintenance easier. There are several types of gutter guards, each with their own advantages and best use cases. The most common types of gutter guards that we encounter include:

Mesh Screen Guard

- Effective at keeping out leaves and large debris.
- Smaller debris like pine needles can still get through the mesh.
- Need hose to clean.
- May need to remove sections for proper cleaning.

Foam Gutter Guards

- Great for keeping out large debris
- Small debris tends to build up on top and must be wiped off to allow water in"""
    },
    # Page 18: Types of Gutter Guards (Part 2)
    {
        "title": "Types of Gutter Guards (Continued)",
        "content": """Gutter Helmet

- Prevents large debris
- Great for heavy rainfall
- Very hard to clean and requires use of hose"""
    },
            # Page 19: Employee Action Plan (Part 1)
    {
        "title": "Employee Action Plan",
        "content": """Objective: To provide a clear, step-by-step guide for employees to follow once they arrive at a job site to ensure safety, efficiency, and customer satisfaction during the window cleaning process.

1. Morning Arrival

- Upon arriving at the shop, read through all work orders for the day. Note any services to be done at each job, and other notes that may require special preparation and equipment.
- Make sure to have all necessary tools and equipment packed. Anticipate add-ons.
- Grab required paperwork (Scratched Glass Waiver, Damage Waiver, etc.)
- Check that ladders are secured properly.
- Check that vehicles are in good and safe use. Report any alerts or damages to Kale immediately.

2. Arrival and Site Assessment

2.1. Arrive on Time and Prepare

- Arrive on the job site on time, ready to work with a positive attitude.
- If for any reason the crew is going to be late, notify the manager right away.

2.2. Greeting the Client

- Greet the client courteously, confirming the scope of work and any specific instructions: "Hello, my name is [Dale] and this is [Craig]. We are the (window/gutter) cleaners from KW Outdoor Solutions."
- After greeting the client, confirm the scope of work that they would like done: "I see on our work order we are here to clean the (e.g., outside windows only/gutters). Is that correct?"
- Upon confirming work, have one employee start taking off screens, unloading equipment, getting out gutter cleaning hoses, etc.
- During this time, have the other employee explain to the client the process as follows, e.g., "[Dale] will start working on the back of the home, while [Craig] works on the front. After the outside windows are cleaned, we will clean the screens and put them back into the windows. Then, we will double-check that the windows are closed and locked."
    },
    # Page 20: Employee Action Plan (Part 2)
    {
        "title": "Employee Action Plan (Continued)",
        "content": """2.3. Site Assessment

- Confirm which areas need cleaning (exterior, interior, etc).
- Each employee must walk around and inspect the area before beginning, looking for any potential hazards (e.g., wet surfaces, furniture placement, or obstructions).
- Note any areas where it is too dangerous to put a ladder without someone footing it.
- Check for any pre-existing damage to the windows/gutters/other (e.g., cracks, chips, or broken seals).
- If working at heights, ensure the area is clear and there is adequate space for ladders and safety equipment.

2.4. Communicate Issues

- After site assessment, talk to the client before beginning any work if concerns are apparent.
- Communicate any matters about pre-existing damage.
- Communicate any matters about inability to clean a certain area/window.
- Inform them of the risk of moving forward, and have them sign a Scratched Glass or Damage Waiver, if they agree to proceed.

3. Determine Start & Stop Locations

- The goal is to complete work in an efficient manner. Determine where each person should start work and stop work. Organize this depending on the anticipated speed of each cleaner, the size of each ladder being used, where the sun is and where it will be, etc.
- The goal is for each crew member to finish at the same time. It also helps with overlapping and work being done twice

4. Begin Cleaning

- Start cleaning (windows/gutters)
- Follow plan as discussed with other employees
- Communicate with other employees as barriers present themselves

4. Post-Cleaning Process

4.1. Inspect the Work

- After completing the cleaning, carefully inspect all windows for streaks, smudges, or areas that may have been missed; or that all gutters are clean.
- Double-check that all surfaces, including window sills and frames, are clean and dry.
- Ensure there is no water or cleaning solution on the floors, furniture, or surrounding areas."""
    },
    # Page 21: Employee Action Plan (Part 3)
    {
        "title": "Employee Action Plan (Continued)",
        "content": """4.2. Clean the Work Area

- Remove any ladders
- Collect all tools, equipment, and any trash from the job site.
- Wipe down all tools, including squeegees, scrubbers, and empty buckets before packing them away for the next job.

5. Client Communication and Feedback

5.1. Client Walkthrough

- Walk the client through the job, showing them the areas that were clean and addressing any concerns they may have.
- Offer to clean any areas the client feels need additional attention.

5.2. Address Any Issues

- If any issues arise (e.g., stubborn stains that couldn't be removed, window damage), discuss them with the client. If damage occurred, fill out the Damage Incident Waiver, and inform the client that a manager will be in touch to discuss further action.

5.3. Request Feedback

- Politely ask the client for feedback on the job and if they were satisfied with the service.
- If the client is happy, ask if they would be willing to leave a review or refer your services to others.

6. End of Job Checklist

- Completed thorough cleaning of all requested services.
- Cleaned and inspected all screens (if applicable).
- Cleaned and inspected all tracks (if applicable).
- Removed all tools and equipment from the job site.
- Properly loaded and secured all ladders for safe transit.
- Client walked through the job to confirm satisfaction.
- Discussed any damage concerns with the client (if applicable).
- Have the client sign a Satisfaction Form.
- Asked the client about leaving a yard sign.
- Ensured that no debris or cleaning materials were left behind."""
    },
    # Page 22: Employee Action Plan (Part 4)
    {
        "title": "Employee Action Plan (Continued)",
        "content": """By following this action plan, employees will ensure a professional, safe, and efficient window cleaning service. This will help maintain high standards of quality and client satisfaction while promoting a safe work environment."""
    },
    # Page 23: Window Cleaning Manual (Part 1)
    {
        "title": "Window Cleaning Instruction Manual",
        "content": """Overview of Window Cleaning:

Window cleaning is essential for maintaining the aesthetic appeal and functionality of windows. Regular cleaning helps to remove dirt, grime, and other contaminants, improving visibility, increasing the lifespan of the windows, and enhancing the overall appearance of the building. Professional window cleaning requires attention to detail, the proper use of tools, and adherence to safety protocols.

Preparing for Window Cleaning:

1. Prepare the Work Area:

- Remove Screens: Prior to cleaning, remove all screens and set them off to the side
- Clear Obstacles: Move any furniture, décor, or other objects away from the windows to prevent them from getting wet or damaged.
- Inspect Windows: Before starting, inspect the windows for any existing damage (cracks, broken seals, or chips).

2. Prepare the Cleaning Solution:

- Mix the Cleaning Solution: Fill a bucket with warm water and add a small amount of soap (about 2-3 drops per gallon of water).
- Stir the Solution: Mix well to create a soapy solution that will clean and break down the dirt on the windows.

Step-by-Step Guide:

1. Apply the Cleaning Solution:

- Dampen the Wet Wand: Dip the wand into the cleaning solution. Wring it out so it's damp but not dripping.
a. If working inside, shake the wand so the excess water does not drip inside home.
- Apply to Glass: Start at the top of the window and apply the cleaning solution using a back-and-forth or up-and-down motion. This will loosen dirt, grime, and dust. Make sure to cover the entire surface, including the edges and corners.
- Scrub Glass: With a piece of 0000 steel wool, take a piece and scrub down the entire pane of glass. Making sure to hit all the edges."""
    },
    # Page 24: Window Cleaning Manual (Part 2)
    {
        "title": "Window Cleaning Instruction Manual (Continued)",
        "content": """2. Use the Squeegee (S-motion):

- Starting Point: Begin at the top left or right corner of the window, holding the squeegee at a slight angle to the glass.
- Squeegee Stroke: Pull the squeegee down in a single stroke at a slight angle and rotate back up. Gradually make your way down the glass until closing out at the bottom.
- Clean the Blade: After each window, wipe the squeegee blade with a clean microfiber cloth to prevent dirt from transferring back onto the window.
- Repeat the Process: Continue to squeegee the window, working from the top to the bottom, ensuring each stroke is slightly overlapping the previous one.

3. Detailing:

- Dry the Edges: After squeegeeing, use a clean, dry microfiber cloth to wipe down the edges of the window to catch any remaining water or streaks.
- Check for Streaks: If there are any streaks, use a dry microfiber cloth, or 0000 dry steel wool to buff them out.
- Drips: Wipe up any excess water to avoid leaving stains or further messes.

4. Screen Cleaning (if applicable)

- If screens need cleaning, use a gentle cleaning solution or water to clean them. Be cautious when handling screens that may have pre-existing damage, as they could be bent or fragile.

5. Track & Sill Cleaning (if applicable)

- If tracks/sills need cleaning, use a gentle cleaning solution or water to clean them. Use a track tool and microfiber towel to remove dirt and grime. Wipe up any excess water.

Special Situations and Techniques:

1. Tinted Windows

- If the client has tinted windows, do not use anything abrasive on them to clean. Only water, soap, and squeegee.

2. Removing Stubborn Stains:

- For paint, sap, or hard water stains that won't come off with a regular cleaning solution, use a razor blade or scraper. Hold the blade at a low angle (about 10-15 degrees) and gently scrape the stain off, making sure to keep the glass wet to avoid scratches."""
    },
    # Page 25: Window Cleaning Manual (Part 3)
    {
        "title": "Window Cleaning Instruction Manual (Continued)",
        "content": """Troubleshooting and Tips for Streak-Free Windows:

- Streaks on Windows:
- Check that squeegee rubber is not ripped. Often the cause.
- Ensure you are pressing the squeegee evenly on glass, and not moving too fast.
- If it's really sunny, re-wet the glass after scrubbing before squeegeeing. Soap drying on glass will leave behind streaks and residue marks
- Water Spots:
- If water spots are left after cleaning, re-wash the window. Might take a few tries. Use a scraper if needed.
- For windows that have years of hard water stains, strong chemicals might be required.
- Cleaning with Too Much Solution:
- Avoid using too much cleaning solution. Excess soap can leave behind a residue.
- If inside, avoid using too much water on wet wands as it can drip onto furniture or floors.

Conclusion:

By following these professional window cleaning instructions, employees will be able to clean windows efficiently and effectively while ensuring a streak-free finish. Always prioritize safety and make sure to maintain equipment properly. Regular window cleaning not only enhances the appearance of the building but also helps prolong the life of the windows."""
    },
    # Page 26: Gutter Cleaning Manual (Part 1)
    {
        "title": "Gutter Cleaning Instruction Manual",
        "content": """Overview of Gutter Cleaning:

Gutter cleaning is a crucial part of maintaining a building's exterior. Clogged gutters can lead to water damage, foundation issues, and landscaping erosion. This manual provides step-by-step instructions for safely and effectively cleaning gutters to ensure proper water flow and prevent damage.

Preparing for Gutter Cleaning:

1. Prepare the Work Area:

- Ladders: Place ladders in a secure area.
- Tools: Gather all tools and necessary equipment.

Step-by-Step Guide:

1. Remove Large Debris:

- Use a gutter hawg or gloved hands to remove leaves, twigs, and dirt.
- Place debris into a bucket or yard waste bag on the ground for disposal.
- Work from one end of the gutter to the other.

2. Flush the Gutters

- Use a garden hose to rinse out smaller debris and dirt.
- Start from the opposite end of the downspout to ensure proper drainage.
- Check for leaks or sagging sections while rinsing.

3. Check and Clear Downspouts

- Ensure water flows freely through downspouts.
- If clogged, snake the downspouts until the clog is gone.
- Check for leaks or sagging sections while rinsing.

4. Inspect

- Check for holes, leaks, or sagging sections."""
    },
    # Page 27: Gutter Cleaning Manual (Part 2)
    {
        "title": "Gutter Cleaning Instruction Manual (Continued)",
        "content": """5. Cleanup

- Give gutters a final rinse to confirm proper water flow.
- Rinse any siding, exterior of gutters, or flat surfaces that may have gotten dirty.
- Clean up debris and put it in the yard waste bag.
- Dispose of debris properly.

6. Post-Cleaning Maintenance Tips

- Advise homeowners to check gutters seasonally.
- Inspect gutters after storms for any new debris buildup.

Conclusion

Proper gutter cleaning is essential for preventing costly water damage. By following this manual, employees will ensure a thorough, safe, and efficient gutter cleaning service. Always prioritize safety, use the right tools, and maintain professionalism while working on a client's property."""
    },
    # Page 28: Identifying and Reporting Damage (Part 1)
    {
        "title": "Identifying and Reporting Damage Caused by Employees",
        "content": """We pride ourselves on professionalism, quality service, and customer satisfaction. Accidents can happen during window cleaning, house washing, or other services, and it's important for employees to follow proper procedures if any damage occurs. This manual outlines the steps employees must take when they identify or cause damage to property, ensuring transparency and prompt resolution.

1. Introduction to Damage Reporting

While we work hard to ensure the safety of your home and property, accidents or unintentional damage may occur during the course of performing our services. When such damage happens, it is critical that employees take immediate action to notify the customer, fill out the necessary forms, and notify their manager for proper handling and resolution.

2. Types of Damage to Report

Employees must be vigilant and immediately report any damage that occurs while on the job site. Examples of damage that must be reported include, but are not limited to:

- Broken Windows
- Broken Grilles or Grids
- Ripped Screens.
- Damaged Window Frames or Trim
- Scratches on Glass
- Bent Gutters
- Etc..

3. Steps to Follow When Damage Occurs

A. Notify the Homeowner Immediately

- First Priority: Inform the client about the damage before leaving the property. This shows professionalism and transparency and allows the homeowner to be aware of any issues firsthand.
- Present the Damage: Clearly point out the damage to the client. Allow them to inspect the damage and ask questions if necessary.
- Apologize for the Inconvenience: Acknowledge the issue with empathy. Let the client know you understand the inconvenience this may cause, and that we will take care of it."""
    },
    # Page 29: Identifying and Reporting Damage (Part 2)
    {
        "title": "Identifying and Reporting Damage Caused by Employees (Continued)",
        "content": """B. Complete the Employee Damage Waiver

- Fill Out the Damage Waiver: Use the company's Employee Damage Waiver form to document the incident. This form will collect essential information about the damage, including:
- Date and time of the incident.
- Type of damage (e.g., broken window, ripped screen).
- Location of the damage (which window, screen, or grille).
- A detailed description of how the damage occurred.
- Sign the Waiver: As the employee reporting the damage, you must sign the waiver. The homeowner should also be asked to sign to acknowledge that they have been informed about the damage.
- Submit to Manager: Once completed, immediately submit the waiver to your manager for further action.

C. Gather Evidence

- Take Photos: Before doing anything else, take clear, high-quality photos of the damage from multiple angles. These photos will help document the damage and serve as evidence.
- Measure the Damage: If applicable, measure the dimensions of the damaged area. For example:
- If a window is broken, measure the size of the glass.
- If a screen is torn, measure the size of the rip and the screen dimensions.
- Record Additional Details: Note any other relevant details, such as whether the damage occurred during routine cleaning or due to specific circumstances like the use of tools.

D. Notify Your Manager

- Inform Your Manager Immediately: As soon as the damage has been documented, call or message your manager to notify them about the incident. Provide them with all the relevant details, including:
- Type of damage.
- Photos of the damage.
- Measurements, if applicable.
- Details from the waiver form.
- Discuss the Next Steps: The manager will review the situation and decide on the appropriate next steps, including possible repairs or resolution with the client."""
    },
    # Page 30: Identifying and Reporting Damage (Part 3)
    {
        "title": "Identifying and Reporting Damage Caused by Employees (Continued)",
        "content": """E. Follow-Up with the Customer

- Professional Follow-Up: After notifying your manager, ensure that the client is aware of the next steps. Your manager will work with the customer to resolve the damage, but keeping the homeowner informed is key to maintaining trust and transparency.
- Resolve as Quickly as Possible: The manager will provide instructions on whether repairs or replacement need to be arranged, or if any compensation is necessary.

4. Important Tips for Employees

- Be Honest and Transparent: If you cause damage, take responsibility and report it immediately. Honesty is key to maintaining a good relationship with our clients.
- Don't Attempt to Fix the Damage: Unless instructed by your manager, do not attempt to fix the damage yourself.
- Maintain Professionalism: Keep a calm and professional demeanor when addressing the customer. Apologize, but do not make excuses for the damage. Focus on solutions.
- Document Everything: Always document everything in detail. This includes the damage, the steps you took, the photos, and any other relevant information. This protects both you and KW Outdoor Solutions."""
    },
    # Page 31: Callbacks and Re-work (Part 1)
    {
        "title": "Callbacks and Re-work for Employees",
        "content": """At KW Outdoor Solutions, we strive to provide exceptional service to our clients on the first visit. However, in some cases, a client may request additional work or a callback to address issues that were not initially resolved. It is crucial that all employees understand the proper protocol for handling callbacks and rework, ensuring that our service quality remains high and that the process is efficient and professional.

1. Definition of a Callback

A callback occurs when a client contacts KW Outdoor Solutions after a service has been completed, requesting additional work to be done due to perceived issues with the original service. Common reasons for callbacks may include:

- Inconsistent Cleaning: Areas that were missed, streaked, or not fully cleaned during the original service.
- Improper Installation: For services like window cleaning, if the screens were improperly re-installed.
- Customer Dissatisfaction: Any concerns or dissatisfaction expressed by the client about the quality of service provided.

Note: A callback is typically requested within a reasonable period (i.e., within 7 days of completing the service) and must be handled in accordance with our company standards.

2. Employee Responsibilities During a Callback

When a callback is requested, employees must follow a clear and professional process to address the situation. Here is the step-by-step protocol:

A. Acknowledge the Callback Request

- Revisit the Property: Visit the client's location as soon as possible to inspect and evaluate the issue. Ensure that the problem is clearly identified and that it falls within the scope of the original service.
- Show Empathy: Apologize for any inconvenience caused and reassure the client that we will resolve the issue to their satisfaction.
- Address the Issue Professionally: Fix the issue thoroughly, ensuring that the original job is completed correctly. Double-check your work to ensure there are no other areas requiring attention.
- Documentation: If necessary, take photos of the areas needing attention and any changes made to resolve the issue."""
    },
    # Page 32: Callbacks and Re-work (Part 2)
    {
        "title": "Callbacks and Re-work for Employees (Continued)",
        "content": """B. Communicate with the Client

- Review the Work: Once the rework is completed, walk the client through the job and ensure that they are satisfied with the results.
- Confirm Satisfaction: Ask the client if everything has been taken care of to their expectations. If they are satisfied, thank them for their understanding and confirm that the matter has been resolved.
- Feedback: Encourage the client to provide feedback on the process. This helps us improve our services and prevents similar issues in the future.

3. Callback and Rework Policy

Compensation and Callback Deductions

- No Charge for Callbacks Within Scope: Callbacks that are a result of errors or missed areas during the original service will not result in additional charges for the client. These are considered part of our commitment to providing excellent service and ensuring customer satisfaction.
- Deduction from Employee Bonus: Employees will receive a deduction from their monthly bonus if the callback is caused by negligence, poor work quality, or failure to follow proper procedures. This deduction will be defined in the EMPLOYEE AGREEMENT AND CONTRACT REGARDING LOST EQUIPMENT AND CALLBACKS waiver.
- Tracking and Accountability: All callbacks will be logged in the company's system to track trends and patterns. If an employee experiences a high number of callbacks, they may need additional training or coaching to improve service quality.

4. Preventing Callbacks and Rework

The best way to minimize callbacks and rework is to complete the job right the first time. Here are a few tips for preventing callbacks:

- Attention to Detail: Double-check all work before finishing the job. Ensure every window, surface, and area is thoroughly cleaned or serviced.
- Clear Communication: Listen to the client's instructions and preferences, and clarify any questions or uncertainties before starting the job. If you are unsure about something, ask your manager for guidance.
- Use the Proper Techniques and Tools: Always use the correct tools, techniques, and safety measures for each job to ensure optimal results and avoid mistakes.
- Take Your Time: Avoid rushing the job. Take the necessary time to complete each task to the best of your ability."""
    },
    # Page 33: Callbacks and Re-work (Part 3)
    {
        "title": "Callbacks and Re-work for Employees (Continued)",
        "content": """5. Quality Control and Continuous Improvement

- Regular Review of Callbacks: Managers will periodically review the details of callbacks to identify any patterns or areas for improvement. This information will be used to provide feedback and training to employees.
- Ongoing Training: KW Outdoor Solutions is committed to continuous improvement. Employees will receive ongoing training to enhance their skills and reduce the likelihood of errors that may lead to callbacks.

6. Conclusion

Callbacks and rework are part of any service industry, but at KW Outdoor Solutions we focus on minimizing them through excellent service, attention to detail, and constant improvement. By following the procedures outlined above and ensuring the highest standards of quality in every job, we can reduce the number of callbacks and provide a superior customer experience.

It is important to understand that callbacks are not an opportunity to be penalized, but an opportunity to learn, grow, and continuously improve our service. By addressing issues proactively and professionally, we will maintain our reputation as a leading provider of window cleaning, gutter cleaning, house washing, and holiday light services."""
    },
    # Page 34: Handling Upset Clients (Part 1)
    {
        "title": "Handling Upset Clients",
        "content": """At KW Outdoor Solutions, we pride ourselves on providing exceptional customer service and fostering positive relationships with our clients. Sometimes, despite our best efforts, clients may become upset or dissatisfied. As an employee, it is essential to handle these situations professionally, with empathy, and a focus on finding a resolution. This section provides guidelines on how to handle upset or difficult clients effectively.

1. Remain Calm and Professional

The first and most important step when dealing with an upset client is to stay calm. Do not take the client's frustration personally. It is important to maintain professionalism at all times, even if the client becomes upset.

Key Points:

- Stay composed: Keep your voice calm, avoid raising your voice, and maintain a neutral, respectful tone.
- Don't get defensive: The client's frustration may not be a reflection of your actions, but more about their expectations or circumstances. Listen without immediately defending the situation.

2. Actively Listen to the Client's Concerns

The client wants to feel heard and understood. By actively listening, you show empathy and respect for their concerns, which can often de-escalate the situation. Here's how to actively listen:

Key Points:

- Give them time: Allow the client to express their concerns fully without interrupting. Even if they are upset, do not cut them off.
- Use body language: If in person, make eye contact, nod, and use open body language to show you are engaged and listening.
- Acknowledge their feelings: Use phrases like, "I can see how that would be frustrating," or "I understand why you are upset.""""
    },
    # Page 35: Handling Upset Clients (Part 2)
    {
        "title": "Handling Upset Clients (Continued)",
        "content": """3. Apologize Sincerely

Once the client has expressed their concerns, offer a sincere apology. It is essential to apologize even if you don't believe you made an error. The apology is about acknowledging the client's feelings and making them feel respected.

Key Points:

- Take responsibility: If there was an issue/damage, acknowledge it and apologize for the inconvenience caused.
- Example: "I'm sorry that you weren't satisfied with our service today. I can understand why that is frustrating."
- Example: "I am sorry I ripped your window screen. I will notify my manager immediately and we will take steps to resolve the problem."
- Avoid empty apologies: Do not simply say "sorry" without offering a solution or taking responsibility where necessary.

4. Ask Clarifying Questions

Once you have apologized, ask for clarification to better understand the specific issue. This allows you to pinpoint the problem and determine the best course of action.

Key Points:

- Be specific: Ask for details about the problem so you can fully understand it.
- Example: "Can you show me exactly what went wrong? Was it a missed area? Or was there an issue with the cleaning?"
- Don't assume: Do not make assumptions about what went wrong. Ask questions to get the full picture.

5. Offer a Solution or Resolution

Once the problem is fully understood, the next step is to offer a solution. Take action as quickly as possible to resolve the issue. If the issue requires time, make sure to communicate that clearly and provide a realistic timeline.

Key Points:

- Present options: If possible, offer more than one solution so the client feels like they have some control over the outcome.
- Example: "I can clean that area again today, or we can schedule a time that is convenient for you. What works best for you?" """
    },
    # Page 36: Handling Upset Clients (Part 3)
    {
        "title": "Handling Upset Clients (Continued)",
        "content": """- Be clear and realistic: Be transparent about the steps you will take and set expectations regarding timing and outcomes.
- Escalate if needed: If you cannot resolve the issue yourself, escalate the situation to a supervisor or manager. Be sure to communicate clearly to the client that you are involving a higher authority to ensure their satisfaction.

6. Ensure the Client Feels Valued

Throughout the interaction, make sure the client feels valued and respected. Often, clients just want to feel that their concerns matter. Going the extra mile in showing care and empathy can turn a negative experience into a positive one.

Key Points:

- Express gratitude: Thank the client for bringing the issue to your attention and giving you the opportunity to fix it.
- Example: "Thank you for your patience as we work to resolve this. We appreciate your feedback, and we'll make sure it doesn't happen again."
- Follow through: After the issue is resolved, ensure that you follow up (if necessary) to confirm the client is satisfied with the outcome.

7. Document the Issue

After dealing with the upset client, it is important to document the situation. This allows the company to track client issues and provide better service in the future.

Key Points:

- Complete a report: Fill out an incident report that includes:
- A detailed description of the issue
- The steps taken to resolve it
- Any follow-up actions (if necessary)
- Notify a manager: If the situation escalated or involved significant issues, inform your manager about the situation and the resolution."""
    },
    # Page 37: Handling Upset Clients (Part 4)
    {
        "title": "Handling Upset Clients (Continued)",
        "content": """8. Learn and Improve

Every difficult situation is an opportunity to learn. After handling a challenging client, take time to reflect on the experience. Discuss the situation with your manager or colleagues, and consider what could have been done differently to improve the outcome.

Key Points:

- Self-reflection: Think about what went well and what could be improved in handling the client.
- Team discussion: If you encounter a new or challenging situation, share it with your team during meetings to help everyone learn and improve.

9. When to Escalate to Management

While most issues can be resolved by following the above steps, some situations may require escalation to management. Here are scenarios where escalation is necessary:

- The client is unreasonably demanding: If the client becomes aggressive, rude, or unreasonable, it is important to involve a manager to ensure the situation does not escalate further.
- The client insists on a refund or compensation: If a client demands compensation that falls outside the scope of company policy, notify a manager to handle the situation.
- Repeated issues: If the same client raises multiple concerns about the same job or if the issue continues to repeat, escalate it to a supervisor for a thorough review.

10. Summary: The Key to Handling Difficult Clients

Handling upset or difficult clients requires empathy, professionalism, and a commitment to finding a solution. When you:

1. Stay calm and listen actively to their concerns,
2. Apologize sincerely for any issues,
3. Offer solutions to resolve the problem,
4. Follow up to ensure their satisfaction,

you turn a potentially negative experience into an opportunity to build trust, enhance customer loyalty, and maintain the high standards of service that KW Outdoor Solutions is known for. Always remember that your professionalism and willingness to resolve any issues make all the difference in maintaining a strong client relationship."""
    },
    # Page 38: Client/Employee Waivers (Glass Scratch Waiver Part 1)
    {
        "title": "GLASS SCRATCH WAIVER",
        "content": """This Damage Waiver and Liability Release ("Agreement") is entered into by and between KW Outdoor Solutions, hereafter referred to as "Company," and the undersigned client, hereafter referred to as "Client," for window cleaning services provided by the Company.

WHEREAS, the Client has requested window cleaning services from the Company, which may involve the use of a razor blade to remove construction materials, paint, stickers, hard water stains, or other debris that cannot be easily removed with conventional cleaning methods; and

WHEREAS, the Client acknowledges and understands that despite the Company's best efforts and care, the use of a razor blade or similar tools may present a risk of causing damage to the window, such as scratches, scuff marks, or other imperfections on the glass surface.

NOW, THEREFORE, in consideration of the mutual promises and the window cleaning services to be rendered, the parties agree as follows:

1. Acknowledgment of Risk

The Client acknowledges and agrees that in the process of cleaning windows, the Company's technicians may use a razor blade or other appropriate tools to remove construction materials, paint, stickers, hard water stains, or other stubborn debris. The Client understands that while the Company will exercise care and proper technique during the cleaning process, there is a possibility that using a razor blade may result in scratches, scuff marks, or other damage to the window glass.

2. Liability Waiver

The Client hereby releases and discharges KW Outdoor Solutions, its employees, contractors, and agents from any and all liability, claims, or damages arising out of or in connection with any potential damage to the windows, including but not limited to scratches, marks, or other defects caused by the use of a razor blade or other cleaning tools required to remove construction materials, paint, stickers, hard water stains, or similar debris.

The Client acknowledges that the use of a razor blade or other tools is sometimes necessary to remove certain materials that cannot be removed through traditional window cleaning methods. The Client agrees to accept the risks associated with this cleaning process.

3. Use of Razor Blades and Tools

The Company's technicians will use razor blades or other similar tools only when necessary to remove construction materials, paint, stickers, hard water stains, or other debris that cannot be removed by standard cleaning techniques. The technicians will use these tools with the utmost care to minimize the risk of any damage. However, the Client understands that despite precautions, scratches, or marks may occur on the window surface."""
    },
    # Page 39: Glass Scratch Waiver (Part 2)
    {
        "title": "GLASS SCRATCH WAIVER (Continued)",
        "content": """4. Client's Consent

By signing this waiver, the Client consents to the use of razor blades or similar tools during the window cleaning process and acknowledges the associated risks. The Client agrees to hold KW Outdoor Solutions, its employees, and agents harmless from any claims, losses, or damages arising from the use of razor blades or other tools during the window cleaning process.

5. Exceptions

This waiver does not release KW Outdoor Solutions from liability for gross negligence, willful misconduct, or failure to adhere to standard industry practices. Any damages not caused by the use of a razor blade or other tools as described above, such as pre-existing window damage, structural defects, or inherent flaws in the window glass, are not covered under this waiver.

6. Agreement

By signing below, the Client agrees to the terms of this Damage Waiver and Liability Release. The Client confirms that they have read and understood the contents of this agreement and voluntarily accept the risks involved in the window cleaning process, including the use of razor blades and other tools when necessary.

Client Name:

Client Signature:

Date:

Technician (if applicable):

Date:

This waiver should be signed prior to the use of razor blades or other tools to ensure the Client is aware of and agrees to the risks involved."""
    },
    # Page 40: Damage Waiver (Part 1)
    {
        "title": "DAMAGE WAIVER AND LIABILITY RELEASE",
        "content": """This Damage Waiver and Liability Release ("Agreement") is entered into by and between KW Outdoor Solutions, hereafter referred to as "Company," and the undersigned client, hereafter referred to as "Client," for window cleaning services provided by the Company.

WHEREAS, the Client has requested window cleaning services from the Company, which may involve the cleaning of windows, screens, and associated hardware; and

WHEREAS, the Client acknowledges and understands that the Company's technicians will take all reasonable care in performing the requested services, but there may be pre-existing conditions of the windows, screens, and hardware that the Company is not liable for, such as damage to the window glass, screens, seals, locks, or other components;

NOW, THEREFORE, in consideration of the mutual promises and the window cleaning services to be rendered, the parties agree as follows:

1. Acknowledgment of Pre-Existing Conditions

The Client acknowledges that KW Outdoor Solutions is not responsible for any pre-existing damage to the following:

- Damage to screens (e.g., bent or broken screens)
- Issues caused by windows that are painted shut or sealed
- Pre-existing scratches, chips, or cracks in the glass
- Pre-existing broken window seals or foggy glass
- Pre-existing broken window locks, control devices, window-related hardware, including but not limited to window cranks or latches.
- Old storm windows separating from the framing
- Bent or distorted storm windows

2. Liability Waiver

The Client hereby releases and discharges KW Outdoor Solutions, its employees, contractors, and agents from any and all liability, claims, or damages arising out of or in connection with any pre-existing damage to the windows, screens, seals, locks, or any other parts of the window or related components.

The Client agrees that the Company is not responsible for any damage to pre-existing issues, including but not limited to:

- Damage to screens (e.g., bent or broken screens)
- Issues caused by windows that are painted shut or sealed"""
    },
    # Page 41: Damage Waiver (Part 2)
    {
        "title": "DAMAGE WAIVER AND LIABILITY RELEASE (Continued)",
        "content": """- Pre-existing scratches, chips, or cracks in the glass
- Pre-existing broken window seals or foggy glass
- Pre-existing broken window locks, control devices, window-related hardware, including but not limited to window cranks or latches.
- Old storm windows separating from the framing
- Bent or distorted storm windows

The Client acknowledges that the Company will take reasonable precautions to avoid causing additional damage during the cleaning process. However, the Client understands that existing issues with the windows, screens, or related components could be exacerbated during cleaning, and the Company is not liable for such occurrences.

3. Client's Consent

By signing this waiver, the Client acknowledges and consents to the cleaning of windows and related components that may have pre-existing conditions. The Client agrees to hold KW Outdoor Solutions, its employees, and agents harmless from any claims, losses, or damages arising from the cleaning of windows or related components with known or unknown pre-existing conditions.

4. Exceptions

This waiver does not release KW Outdoor Solutions from liability for gross negligence, willful misconduct, or failure to adhere to standard industry practices during the cleaning process. Any damages not caused by pre-existing conditions, such as damage resulting from improper handling or negligence, will remain the responsibility of the Company.

5. Agreement

By signing below, the Client agrees to the terms of this Damage Waiver and Liability Release. The Client confirms that they have read and understood the contents of this agreement and voluntarily accept the risks involved in the window cleaning process, including the pre-existing conditions of the windows, screens, and hardware."""
    },
    # Page 42: Damage Waiver (Part 3)
    {
        "title": "DAMAGE WAIVER AND LIABILITY RELEASE (Continued)",
        "content": """Client Name:

Client Signature:

Date:

Technician (if applicable):

Date:

This waiver should be signed prior to any window cleaning services to ensure that both the client and the company understand and agree to the potential risks associated with pre-existing damage."""
    },
    # Page 43: Employee Damage Report Waiver
    {
        "title": "Employee Damage Report Waiver",
        "content": """Client Name:

Date:

Customer Address:

(Employee) who caused the damage:

Damage Type:

How did the damage occur?

Client Acknowledgment

I, the undersigned homeowner, have been informed of the damage caused during this service. I acknowledge the damage and the employee's report.

Client Name:

Signature:

Date:

Employee Acknowledgment

I, the undersigned employee, confirm that I have reported this damage to the homeowner and followed company procedures.

Employee Signature:

Date:"""
    },
    # Page 44: Emergency Contact Form
    {
        "title": "Emergency Contact Form",
        "content": """Special Instructions:

In the event of a medical emergency, are there any emergency procedures or restrictions on medications of which emergency personnel should be aware? If yes, please explain.

Primary Contact in case of emergency:

Name:

Relationship:

Phone Number:

Alternate Phone:

Number:

Secondary Contact in case of emergency:

Name:

Relationship:

Phone Number:

Alternate Phone:

Number:

Employee Authorization:

I have voluntarily provided the above contact information and authorize KW Outdoor Solutions and its representatives to contact any of the above individuals on my behalf in the event of an emergency.

Employee Signature:

Date:"""
    },
    # Page 45: Vehicle Use Agreement
    {
        "title": "Vehicle Use Agreement For KW Outdoor Solutions",
        "content": """Employee Name:

Driver's License No:

The above named employee is authorized to operate a motor vehicle on company business only under the following conditions:

- He/she follows and fully cooperates with our company's Motor Vehicle Safety Policy.
- He/she maintains a valid driver's license and remains fully insurable.
- He/she operates the vehicle in a safe manner, obeying all traffic laws.
- He/she and all passengers wear their seat belts.
- He/she promptly reports all motor vehicle accidents to his/her supervisor.
- He/she will report any new dents, scratches, or other cosmetic damages caused by the Employee.
- He/she will report any and all safety concerns (i.e. engine lights, faulty brakes, ect.).
- He/she assumes full responsibility for any traffic violations and/or fines arising out of the use of the vehicle.
- He/she understands that personal use of the company-provided vehicle is prohibited.

The use of a company vehicle is an important part of your job. Only you, or other employees permitted to drive, may operate an assigned company vehicle. You will be expected to keep the vehicle clean and in working condition at all times and to promptly report any change in your driver's license status/validity. Any traffic violation may subject you to restricted driving privileges, suspension of driving privileges, or possible loss of employment.

Company management may modify, or revoke this agreement at any time, with or without notice.

I have read, understand, and agree to comply with the above conditions in exchange for being authorized to drive on company business.

Employee Signature:

Date:"""
    },
    # Page 46: Employee Agreement (Lost Equipment and Callbacks, Part 1)
    {
        "title": "EMPLOYEE AGREEMENT AND CONTRACT REGARDING LOST EQUIPMENT AND CALLBACKS",
        "content": """This Agreement is made and entered into by and between KW Outdoor Solutions, hereafter referred to as "Employer," and , hereafter referred to as "Employee," collectively referred to as "Parties."

1. Purpose of Agreement

This agreement outlines the terms and conditions related to the Employer's bonus structure, specifically regarding the loss of equipment and callbacks from job sites. The structure is designed to incentivize proper handling of company property and the successful completion of jobs without callbacks.

2. Bonus Structure

Employee will receive a monthly bonus of $200 (the "Bonus"), which will be paid in the paycheck following the end of each month. The Bonus is subject to the following deductions:

3. Lost Equipment

If any equipment provided by the Employer, including but not limited to squeegees, wet wipes, scrubbers, and tool belts, is lost, damaged, or otherwise rendered unusable due to the Employee's negligence or failure to follow proper care for the equipment, the following procedure will apply:

- A deduction will be made from the Employee's Bonus in the amount of the cost to replace the lost equipment.
- The deduction will be made from the monthly Bonus for the month in which the loss occurred.
- Prices for lost items (tool belt, belt bucket, large & small wet wand, Squeegees, scrubber pad, and water buckets) are listed in the equipment needed section.

4. Callbacks

A "callback" is defined as a situation where the Employer has to send an employee back to a job site due to the quality of work being unsatisfactory or incomplete, as determined by the Employer or customer complaints. For each callback, the following deduction will be made from the Employee's Bonus:

- $25 will be deducted per callback from the Employee's Bonus.
- After three callbacks in a 30 day period, the Employee will be required to complete additional training.
- New employees will be given a three week grace period that begins on their start date.

5. Bonus Deductions Cap

In the event that the total of deductions (from lost equipment and callbacks) exceeds the value of the Bonus ($200), the Employee will not have any further deductions taken from their paycheck beyond the total value of the Bonus. The Employee will not be required to pay any amount out-of-pocket to cover the difference.

6. Payment Schedule

- Deductions for lost equipment and callbacks will be calculated monthly.
- The final amount of the Employee's Bonus, after deductions, will be paid in the paycheck following the end of the month."""
    },
    # Page 47: Employee Agreement (Part 2)
    {
        "title": "EMPLOYEE AGREEMENT AND CONTRACT REGARDING LOST EQUIPMENT AND CALLBACKS (Continued)",
        "content": """7. Employee Responsibilities

- The Employee agrees to take reasonable care of all equipment and tools provided by the Employer.
- The Employee agrees to notify the Employer immediately if any equipment is lost or damaged.
- The Employee agrees to perform all work to the highest standards to minimize the possibility of callbacks.

8. Acknowledgment

By signing below, the Employee acknowledges understanding and agreement to the terms outlined in this Agreement, including the conditions for lost equipment and callbacks, as well as the bonus structure and deductions associated with such occurrences.

9. Termination of Agreement

This Agreement will remain in effect as long as the Employee is employed by the Employer. The Employer reserves the right to amend or terminate this agreement at any time, provided that the Employee is notified of such changes in writing.

[Employer Name]

[Title/Position]

[Company Name]

Date:

[Employee Name]

[Employee Signature]

Date:"""
    },
    # Page 48: Positive Review Bonus Program
    {
        "title": "Positive Review Bonus Program",
        "content": """This program is designed to reward employees for receiving positive feedback from clients after completing a service. Every time an employee receives a positive review, they will be awarded $5 as a token of appreciation for their dedication to delivering exceptional service.

How It Works:

1. Eligibility:

All Cleaning Technicians are eligible to participate in the Positive Review Incentive Program. Employees must maintain employment to remain eligible.

2. Positive Review Definition:

A "positive review" is any rating from a client that is four stars or higher left on the company's Google page.

3. Award Amount:

For each positive review submitted by a client, the employee who completed the service will receive a $5 bonus.

4. Tracking Reviews:

Our management team will track reviews for that pay period and the bonus will be paid on the corresponding pay day.

Additional Notes:

- Positive reviews are essential to the continued success of our business, as they help build our reputation and attract new customers. Your participation in this program is crucial to maintaining a high level of customer satisfaction.
- Employees can accumulate multiple bonuses over time. There is no cap on how many reviews you can earn bonuses for.
- This program is subject to change based on business needs and performance. Employees will be notified if any adjustments are made.

Employee Signature:

Date:"""
    },
    # Page 49: Non-Solicitation Clause
    {
        "title": "Non-Solicitation Clause",
        "content": """The Employee agrees that, during the term of their employment with KW Outdoor Solutions and for a period of 24 months following the termination of their employment, whether voluntary or involuntary, they will not, directly or indirectly:

1. Solicit or attempt to solicit any customer, client, or business partner of KW Outdoor Solutions for the purpose of offering or providing services that are similar to or competitive with those offered by KW Outdoor Solutions.

2. Hire or attempt to hire any employee, contractor, or agent of KW Outdoor Solutions to work for any competing business or enterprise.

The Employee acknowledges that the restrictions set forth in this clause are necessary to protect the legitimate business interests of KW Outdoor Solutions, and that these restrictions are reasonable in scope, duration, and geographical area.

Employee Signature:

Date:"""
    },
    # Page 50: New Hire Paperwork
    {
        "title": "New Hire Paperwork",
        "content": """[Placeholder for New Hire Paperwork content, as original document cuts off here.]"""
    }
]

# Function to generate PDF
def create_sop_pdf():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story = []
    
    for i, page in enumerate(sop_pages, 1):
        # Add page title
        story.append(Paragraph(f"{i}", styles["Normal"]))
        story.append(Spacer(1, 0.1 * inch))
        story.append(Paragraph(page["title"], styles["Heading1"]))
        story.append(Spacer(1, 0.2 * inch))
        
        # Add content
        content_lines = page["content"].split("\n")
        for line in content_lines:
            if line.strip():
                # Check if line is a heading (e.g., "1. Morning Arrival")
                if line.strip()[0].isdigit() and "." in line[:3]:
                    story.append(Paragraph(line.strip(), styles["Heading2"]))
                else:
                    story.append(Paragraph(line.strip(), styles["BodyText"]))
                story.append(Spacer(1, 0.1 * inch))
        
        # Add page break (except for the last page)
        if i < len(sop_pages):
            story.append(PageBreak())
    
    doc.build(story)
    buffer.seek(0)
    return buffer

# Streamlit app
st.title("KW Outdoor Solutions SOP")

# Sidebar for TOC
st.sidebar.header("Table of Contents")
toc_entries = sop_pages[0]["content"].split("\n")
selected_page = 1  # Default to page 1

for entry in toc_entries:
    if entry.strip():
        section_name, page_num = entry.rsplit(" ", 1)
        try:
            page_num = int(page_num)
            if st.sidebar.button(f"{section_name} (Page {page_num})"):
                selected_page = page_num
        except ValueError:
            continue

# Page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = 1

# Update current page if a TOC link was clicked
if selected_page != 1:
    st.session_state.current_page = selected_page

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    if st.button("Previous Page") and st.session_state.current_page > 1:
        st.session_state.current_page -= 1
with col2:
    if st.button("Next Page") and st.session_state.current_page < len(sop_pages):
        st.session_state.current_page += 1
with col3:
    st.write(f"Page {st.session_state.current_page} of {len(sop_pages)}")

# Display current page
current_page = sop_pages[st.session_state.current_page - 1]
st.header(current_page["title"])
st.write(current_page["content"])

# Download PDF button
pdf_buffer = create_sop_pdf()
st.download_button(
    label="Download SOP PDF",
    data=pdf_buffer,
    file_name="KW_Outdoor_Solutions_SOP.pdf",
    mime="application/pdf"
)
