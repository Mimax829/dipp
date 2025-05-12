import streamlit as st
import openai

# Set up your OpenAI API key (μέσω Streamlit secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Τίτλος εφαρμογής
st.title("Εντοπισμός Εναλλακτικών Ιδεών με ΤΝ")

# Εισαγωγή ερώτησης φυσικής
question = st.text_input("Ερώτηση φυσικής:", "Τι είναι η δύναμη;")

# Εισαγωγή απάντησης μαθητή (χωρίς προκαθορισμένο κείμενο)
student_answer = st.text_area("Απάντηση μαθητή:")

# Κουμπί Ανάλυσης
if st.button("Ανάλυση απάντησης"):
    if not student_answer.strip():
        st.warning("Παρακαλώ γράψτε μια απάντηση για να γίνει η ανάλυση.")
    else:
        with st.spinner("Ανάλυση με Τεχνητή Νοημοσύνη..."):
            # Prompt προς το AI
            prompt = f"""
Είσαι ένας καθηγητής φυσικής. Η παρακάτω ερώτηση δόθηκε σε μαθητές και η απάντηση τους αναλύεται για την ύπαρξη εναλλακτικών ιδεών.

Ερώτηση: {question}
Απάντηση μαθητή: {student_answer}

Ανίχνευσε αν η απάντηση περιέχει κάποια εναλλακτική ιδέα ή λανθασμένη αντίληψη. Αν ναι, εξήγησε ποια είναι και δώσε μια σύντομη, επιστημονικά ορθή εξήγηση.

Απάντηση:
"""

            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2,
                    max_tokens=300
                )

                reply = response.choices[0].message.content.strip()
                st.subheader("Ανάλυση ΤΝ:")
                st.write(reply)

            except Exception as e:
                st.error(f"Παρουσιάστηκε σφάλμα: {str(e)}") 

