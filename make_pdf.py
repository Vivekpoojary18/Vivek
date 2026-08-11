from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_pdf():
    doc = SimpleDocTemplate(
        "Vivek_J_Poojary_Resume.pdf",
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=8
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=8,
        spaceAfter=4,
        textTransform='uppercase'
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#0f172a')
    )

    item_sub_style = ParagraphStyle(
        'ItemSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        leftIndent=14,
        firstLineIndent=-10,
        textColor=colors.HexColor('#334155'),
        spaceAfter=2
    )

    story = []

    # Title & Contact
    story.append(Paragraph("VIVEK J POOJARY", title_style))
    story.append(Paragraph("Mangaluru, Karnataka, India &nbsp;|&nbsp; vivekjpoojary@gmail.com &nbsp;|&nbsp; +91 82173 67683 &nbsp;|&nbsp; linkedin.com/in/vivekjpoojary &nbsp;|&nbsp; github.com/Vivekjpoojary", contact_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=2, spaceAfter=6))

    # Summary
    story.append(Paragraph("SUMMARY", section_style))
    story.append(Paragraph("Builds and ships systems that turn raw data into decisions — from a retrieval-augmented AI platform serving page-accurate answers across documents to a demand-forecasting engine that directly shapes real-time resource allocation. Track record centers on closing the gap between prototype and production: 33/33 automated tests passing in CI, an 83.3% predictive accuracy benchmark achieved through systematic model comparison, and normalized data architectures built to eliminate redundancy at scale. IBM-certified Data Science practitioner (BCA, CGPA 8.08) seeking an entry-level Data Analyst, Data Science, or AI/ML Engineering role.", body_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=4, spaceAfter=6))

    # Education
    story.append(Paragraph("EDUCATION", section_style))
    story.append(Paragraph("Bachelor of Computer Applications (BCA) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jun 2023 – May 2026", item_title_style))
    story.append(Paragraph("St. Aloysius (Deemed to be University), Mangaluru, Karnataka", item_sub_style))
    story.append(Paragraph("• <b>CGPA: 8.08 / 10.0</b>", bullet_style))
    story.append(Paragraph("• Relevant Coursework: Data Structures, Database Management Systems, Machine Learning Fundamentals, Statistical Analysis, Web Technologies", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=4, spaceAfter=6))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_style))
    story.append(Paragraph("• <b>Programming Languages:</b> Python, SQL, R, Java, JavaScript, PHP, C", bullet_style))
    story.append(Paragraph("• <b>ML / Data Science:</b> Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Predictive Modelling, Feature Engineering", bullet_style))
    story.append(Paragraph("• <b>AI / RAG:</b> FAISS Vector Search, FastEmbed, LLM Integration (Groq), Retrieval-Augmented Generation", bullet_style))
    story.append(Paragraph("• <b>Web Technologies:</b> HTML5, CSS3, JavaScript, React.js, TypeScript, TailwindCSS, PHP, J2EE, REST APIs, FastAPI, Django REST Framework", bullet_style))
    story.append(Paragraph("• <b>Databases:</b> MySQL, SQLite, PostgreSQL (3NF schema design, complex joins, indexing)", bullet_style))
    story.append(Paragraph("• <b>Tools & Platforms:</b> Jupyter Notebook, Git, GitHub, GitHub Actions (CI/CD), Docker-ready deployments (Render, Vercel), VS Code", bullet_style))
    story.append(Paragraph("• <b>Concepts:</b> Machine Learning, Data Analysis, JWT-based Auth & RBAC Systems, Geospatial Visualisation, Automated Testing (pytest)", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=4, spaceAfter=6))

    # Projects
    story.append(Paragraph("PROJECTS", section_style))
    story.append(Paragraph("DocMind AI — Production RAG Document Intelligence Platform", item_title_style))
    story.append(Paragraph("FastAPI | React.js/TypeScript | FAISS | Groq LLM | JWT Auth — github.com/vivekjpoojary/docmind-ai", item_sub_style))
    story.append(Paragraph("• Architected and deployed a full-stack RAG platform (FastAPI + React/TypeScript, live on Render and Vercel) enabling PDF/DOCX/TXT upload and AI-powered Q&A with page-accurate citations.", bullet_style))
    story.append(Paragraph("• Implemented per-user isolated FAISS vector search with FastEmbed embeddings and Groq LLM integration for low-latency retrieval augmented generation.", bullet_style))
    story.append(Paragraph("• Built JWT-based auth with refresh-token rotation and rate limiting; validated with 33/33 automated tests passing via GitHub Actions CI.", bullet_style))

    story.append(Paragraph("PlayPoint — Sports Venue Booking & Analytics Platform", item_title_style))
    story.append(Paragraph("React.js | Django REST Framework | SQLite | Python | Scikit-learn — github.com/Vivekjpoojary", item_sub_style))
    story.append(Paragraph("• Built a full-stack booking platform for real-time court reservations, supporting three permission tiers via a JWT-based Role-Based Access Control system.", bullet_style))
    story.append(Paragraph("• Designed a 3NF-compliant relational schema across nine normalized tables, enforcing referential integrity and eliminating redundant data across all modules.", bullet_style))
    story.append(Paragraph("• Trained a Linear Regression model on historical booking data to predict peak-demand slots, feeding directly into the platform's slot-allocation logic and Matplotlib dashboards.", bullet_style))

    story.append(Paragraph("IBM Data Science Capstone — Falcon 9 Landing Prediction", item_title_style))
    story.append(Paragraph("Python | Pandas | NumPy | Scikit-learn | Matplotlib | Folium", item_sub_style))
    story.append(Paragraph("• Built an end-to-end pipeline — SpaceX REST API ingestion and web scraping, EDA, feature engineering, and modelling — to predict Falcon 9 first-stage landing outcomes.", bullet_style))
    story.append(Paragraph("• Benchmarked four classifiers (Logistic Regression, Decision Tree, SVM, KNN); a GridSearchCV-tuned Decision Tree achieved 83.3% accuracy, the best of the set.", bullet_style))
    story.append(Paragraph("• Built interactive Folium maps to visualise launch-site proximity and surface spatial patterns across historical missions.", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=4, spaceAfter=6))

    # Certifications
    story.append(Paragraph("CERTIFICATIONS", section_style))
    story.append(Paragraph("IBM Data Science Professional Certificate &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Aug 2025", item_title_style))
    story.append(Paragraph("IBM / Coursera", item_sub_style))
    story.append(Paragraph("• 10-course specialisation covering Python, SQL, data visualisation, and machine learning, capped by an applied capstone spanning the full data science lifecycle.", bullet_style))

    story.append(Paragraph("Deloitte Technology Virtual Experience Program &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mar 2026", item_title_style))
    story.append(Paragraph("Forage", item_sub_style))
    story.append(Paragraph("• Completed hands-on modules in Python-based ETL, IIoT data unification, and a software development proposal for a simulated client engagement (Daikibo Industrials).", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#cbd5e1'), spaceBefore=4, spaceAfter=6))

    # Achievements & Activities
    story.append(Paragraph("ACHIEVEMENTS & ACTIVITIES", section_style))
    story.append(Paragraph("• <b>National-Level Wushu & Kung Fu Athlete</b> — Bronze medal, 16th National Kung-Fu Championship; multiple national-level participations demonstrating sustained discipline under competitive pressure.", bullet_style))
    story.append(Paragraph("• <b>Class Representative (2024–25)</b> — Elected student liaison between faculty and peers for a BCA cohort, handling academic communications and scheduling.", bullet_style))

    doc.build(story)
    print("ReportLab PDF built successfully: Vivek_J_Poojary_Resume.pdf")

if __name__ == '__main__':
    build_pdf()
