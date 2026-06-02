import os
import streamlit as st
from agent import ResearchAgent
from report_generator import ReportGenerator
from trace_generator import TraceGenerator

# Set up page configuration
st.set_page_config(
    page_title="ReAct Web Research Agent",
    page_icon="🔍",
    layout="wide"
)

# Ensure the outputs directory exists
os.makedirs("outputs", exist_ok=True)

# ==========================
# CUSTOM UI ENHANCEMENT (CSS)
# ==========================
st.markdown("""
<style>
    /* Global Background and Typography adjustments */
    .stApp {
        background: linear-gradient(180deg, #f8fafd 0%, #f1f5f9 100%);
    }
    
    /* Smooth transitions for buttons and expanders */
    .stButton>button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.8rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3) !important;
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
    }

    /* Elegant Custom Cards for project features & lists */
    .feature-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
    }
    
    .feature-item {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        font-size: 0.95rem;
    }
    
    .feature-icon {
        color: #10b981;
        margin-right: 10px;
        font-weight: bold;
    }

    /* Workflow step tracking bubbles */
    .workflow-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
        background: #1e293b;
        padding: 20px;
        border-radius: 14px;
        color: #f8fafc;
    }
    
    .workflow-step {
        background: rgba(255, 255, 255, 0.07);
        padding: 8px 14px;
        border-radius: 8px;
        text-align: center;
        font-weight: 500;
        font-family: monospace;
        border-left: 4px solid #3b82f6;
    }
    
    .workflow-arrow {
        text-align: center;
        color: #64748b;
        font-size: 1.1rem;
        line-height: 1;
    }

    /* Metrics Section Customizations */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #1e3a8a !important;
    }
    
    [data-testid="stMetricBackground"] {
        background-color: white !important;
        border-radius: 14px !important;
        padding: 15px !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* Clean up headers */
    h1 {
        font-weight: 800 !important;
        color: #0f172a !important;
    }
</style>
""", unsafe_allow_html=True)


# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.title("⚙️ System Info")
    
    st.markdown("### 🤖 Engine Specs")
    st.write("🧠 **Primary:** Gemini 3.1 Flash Lite")
    st.write("⚡ **Reasoning:** Llama 3.3 70B (Groq)")
    st.write("🔎 **Search:** Tavily API")
    
    st.divider()
    
    st.markdown("### 🔄 ReAct Pipeline Execution")
    # Rendering step items using clean HTML divs styled via our injected CSS
    st.markdown("""
    <div class="workflow-container">
        <div class="workflow-step">Thought</div>
        <div class="workflow-arrow">↓</div>
        <div class="workflow-step">Action</div>
        <div class="workflow-arrow">↓</div>
        <div class="workflow-step">Observation</div>
        <div class="workflow-arrow">↓</div>
        <div class="workflow-step">Summary</div>
        <div class="workflow-arrow">↓</div>
        <div class="workflow-step">Memory</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("### 🚀 Engine Capabilities")
    # Clean checkmark layout using styled HTML blocks instead of raw markdown ticks
    st.markdown("""
    <div class="feature-card">
        <div class="feature-item"><span class="feature-icon">✓</span> ReAct Execution Pattern</div>
        <div class="feature-item"><span class="feature-icon">✓</span> Live Web Grounding</div>
        <div class="feature-item"><span class="feature-icon">✓</span> Hybrid LLM Orchestration</div>
        <div class="feature-item"><span class="feature-icon">✓</span> Dynamic Context Memory</div>
        <div class="feature-item"><span class="feature-icon">✓</span> Native Trace Generation</div>
        <div class="feature-item"><span class="feature-icon">✓</span> Compiled Research Synthesis</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================
# MAIN PAGE
# ==========================
st.title("🔍 ReAct Web Research Agent")
st.markdown(
    """
    An advanced research intelligence workspace utilizing the **Reasoning and Acting (ReAct)** core execution architecture.
    """
)

# Wrapping introductory highlights into clean responsive grid items
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown("🤖 **Autononous Scoping**\nFormulates underlying research paths targeted to your prompt.")
with col_b:
    st.markdown("🌐 **Live Information Retrieval**\nQueries, reads, and processes real-time data using Tavily Search.")
with col_c:
    st.markdown("📝 **Synthesis & Compiling**\nGenerates deep-dive multi-perspective analytical output logs.")

st.write("") # Spacer

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Explain Retrieval-Augmented Generation (RAG)"
)


# ==========================
# RUN AGENT
# ==========================
if st.button("🚀 Start Research Workflow"):
    if not topic.strip():
        st.warning("Please specify a valid research topic target to initiate processing.")
    else:
        try:
            with st.spinner("Agent initializing tools, reasoning chains, and accessing external search fabrics..."):
                # Initialize Agent and run pipelines
                agent = ResearchAgent()
                findings = agent.run(topic)
                
                consolidated_report = agent.llm.beautify_report(topic, findings)
                
                report = ReportGenerator().generate(
                    topic,
                    findings,
                    consolidated_report
                )
                
                trace = TraceGenerator().generate(findings)
                
                # Write outputs locally
                with open("outputs/report.md", "w", encoding="utf-8") as f:
                    f.write(report)

                with open("outputs/trace.md", "w", encoding="utf-8") as f:
                    f.write(trace)

            st.success("✨ Analysis lifecycle completed! Assets generated and recorded locally.")

            # ==========================
            # METRICS
            # ==========================
            total_questions = len(findings)
            total_sources = sum(len(entry["sources"]) for entry in findings)

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Total Answered Inquiries", value=total_questions)
            with col2:
                st.metric(label="Aggregated Knowledge Sources Found", value=total_sources)

            st.divider()

            # ==========================
            # QUESTION INSPECTION
            # ==========================
            st.subheader("🧠 Inner-Loop ReAct Steps")
            for entry in findings:
                with st.expander(f"🔮 Dynamic Probe {entry['id']} — {entry['question'][:60]}..."):
                    st.markdown(f"#### ❓ Core Target Inquiry\n{entry['question']}")
                    st.markdown(f"#### 💭 System Thought\n*{entry['thought']}*")
                    st.markdown(f"#### 🛠️ Executed Tool Action\n`{entry['action']}`")
                    st.markdown(f"#### 👁️ Observation Payload\n{entry['observation']}")
                    st.markdown(f"#### 📌 Node Resolution Summary\n{entry['summary']}")

            st.divider()

            # ==========================
            # REPORTS
            # ==========================
            tab1, tab2 = st.tabs(["📄 Finalized Research Report", "🧠 Structural ReAct Trace"])

            with tab1:
                st.markdown(report)
                st.download_button(
                    "⬇ Download Complete Report (.md)",
                    report,
                    file_name="report.md",
                    mime="text/markdown"
                )

            with tab2:
                st.markdown(trace)
                st.download_button(
                    "⬇ Download Execution Trace Log (.md)",
                    trace,
                    file_name="trace.md",
                    mime="text/markdown"
                )

        except Exception as e:
            st.error(f"Execution Interrupted:\n\n{str(e)}")