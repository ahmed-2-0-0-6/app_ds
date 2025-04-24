import streamlit as st
import mysql.connector

# Connect to MySQL using Streamlit secrets
def connect_db():
    return mysql.connector.connect(
        host=st.secrets["database"]["host"],
        user=st.secrets["database"]["user"],
        password=st.secrets["database"]["password"],
        database=st.secrets["database"]["name"]
    )

# UI
st.title("📚 Add New Book")

title = st.text_input("Book Title")
author = st.text_input("Author")
year = st.text_input("Year Published")

if st.button("➕ Add Book"):
    if not title or not author or not year:
        st.warning("Please fill in all fields.")
    else:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Books (title, author, year_published) VALUES (%s, %s, %s)",
                (title, author, int(year))
            )
            conn.commit()
            cursor.close()
            conn.close()
            st.success("✅ Book added successfully!")
        except ValueError:
            st.error("⚠️ Year must be a number.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
