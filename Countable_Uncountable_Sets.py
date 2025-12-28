# Countable_Uncountable_sets
import streamlit as st

def main():
    st.set_page_config(page_title="Discrete Mathematics: Set Theory Lab", layout="wide")
    
    st.title("🎓 Discrete Mathematics Interactive Lab")
    st.subheader("Exploring Finite, Infinite, Countable, and Uncountable Sets")

    # Sidebar Navigation
    menu = ["Important Definitions", "Equivalent Sets & Quiz", "Equivalence Proofs", "Non-Equivalence & Real Numbers", "Practical Examples"]
    choice = st.sidebar.selectbox("Navigate Lessons", menu)

    if choice == "Important Definitions":
        st.header("📖 Core Definitions")
        st.write("""
        As per the syllabus, understanding the nature of sets is fundamental to mathematical reasoning[cite: 521, 579].
        
        * **Finite Set**: A set $A$ is finite if it is empty or if there exists a natural number $n$ such that there is a bijection from $A$ to the set $\mathbb{N}_n = \{1, 2, \dots, n\}$[cite: 521].
        * **Infinite Set**: A set that is not finite[cite: 521].
        * **Denumerable Set**: A set $A$ is denumerable if there exists a bijection $f: \mathbb{N} \to A$.
        * **Countable Set**: A set is countable if it is either finite or denumerable.
        * **Uncountable Set**: An infinite set that is not countable (e.g., the set of real numbers).
        """)

    elif choice == "Equivalent Sets & Quiz":
        st.header("🤝 Equivalent Sets")
        st.info("**Definition**: Two sets $A$ and $B$ are said to be **equivalent** (or equipotent), denoted $A \sim B$, if there exists a bijective function $f: A \to B$.")
        
        st.subheader("Interactive Quiz: Are these sets equivalent?")
        
        # Quiz 1
        q1 = st.radio("1. $A = \{a, b, c\}$ and $B = \{1, 2, 3\}$", ("Select", "Yes", "No"))
        if q1 == "Yes": st.success("Correct! Both have 3 elements, so a bijection exists.")
        elif q1 == "No": st.error("Incorrect. They have the same cardinality.")

        # Quiz 2
        q2 = st.radio("2. $A = \{1, 2\}$ and $B = \{1, 2, 3\}$", ("Select", "Yes", "No"))
        if q2 == "No": st.success("Correct! They have different number of elements.")
        elif q2 == "Yes": st.error("Incorrect. A bijection cannot be formed.")

    elif choice == "Equivalence Proofs":
        st.header("📐 Proofs of Equivalence")
        st.write("We show that several infinite sets have the same cardinality as $\mathbb{N}$.")

        with st.expander("Proof: Natural Numbers $\sim$ Even Natural Numbers"):
            st.write("""
            Let $E = \{2, 4, 6, \dots\}$. 
            Define $f: \mathbb{N} \to E$ by $f(n) = 2n$.
            - **Injective**: If $2n_1 = 2n_2$, then $n_1 = n_2$.
            - **Surjective**: For any even number $2k \in E$, there exists $k \in \mathbb{N}$ such that $f(k) = 2k$.
            Since $f$ is a bijection, $\mathbb{N} \sim E$.
            """)

        with st.expander("Proof: Natural Numbers $\sim$ Integers ($\mathbb{Z}$)"):
            st.write("""
            Define $f: \mathbb{N} \to \mathbb{Z}$ as:
            $f(n) = \\frac{n}{2}$ if $n$ is even, and $f(n) = -\\frac{n-1}{2}$ if $n$ is odd.
            This mapping covers $\{0, 1, -1, 2, -2, \dots\}$, proving $\mathbb{N} \sim \mathbb{Z}$.
            """)

        with st.expander("Proof: Natural Numbers $\sim$ Rational Numbers ($\mathbb{Q}$)"):
            st.write("""
            **Cantor's Zig-Zag Argument**: List all fractions $p/q$ in a 2D grid where rows are $p$ and columns are $q$. 
            By following a diagonal path and skipping duplicates, we can count every rational number.
            Hence, $\mathbb{Q}$ is countable.
            """)

    elif choice == "Non-Equivalence & Real Numbers":
        st.header("🚫 The Uncountable Nature of $\mathbb{R}$")
        
        st.subheader("1. Interval (0,1) is not equivalent to $\mathbb{N}$")
        st.write("""
        **Cantor’s Diagonal Argument**:
        Suppose (0,1) is countable and list them as decimals. We can always construct a new decimal $x$ by changing the $n$-th digit of the $n$-th number in the list. 
        This new $x$ differs from every number in the list, creating a contradiction.
        """)

        st.subheader("2. Interval (0,1) is equivalent to $\mathbb{R}$")
        st.write("""
        We can find a bijection $f: (0,1) \to \mathbb{R}$.
        Example function: $f(x) = \\tan(\pi x - \\pi/2)$.
        As $x$ goes from 0 to 1, the value of $f(x)$ covers all real numbers from $-\infty$ to $+\infty$.
        """)

    elif choice == "Practical Examples":
        st.header("🧪 Practical Problems")
        
        st.markdown("### 1. Notation $\mathbb{N}_n$")
        st.write("$\mathbb{N}_n = \{1, 2, 3, \dots, n\}$. This is used to define finite sets[cite: 521].")

        st.markdown("### 2. Cardinality of Symbols")
        st.write("Show that $S = \{\Delta, \\alpha, \gamma\}$ is finite.")
        st.info("There exists a bijection $f: S \to \mathbb{N}_3$ where $f(\Delta)=1, f(\\alpha)=2, f(\gamma)=3$. Thus, $S$ is finite with cardinality 3.")

        st.markdown("### 3. Binary Matrices")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("2x2 Binary Matrices", "2^4 = 16")
            st.caption("Each of the 4 positions can be 0 or 1.")
        with col2:
            st.metric("3x3 Binary Matrices", "2^9 = 512")
            st.caption("Each of the 9 positions can be 0 or 1.")

        st.markdown("### 4. Bijective Function: $\mathbb{N} \\to \mathbb{Z}$")
        st.latex(r"f(n) = \begin{cases} \frac{n}{2} & \text{if } n \text{ is even} \\ -\frac{n-1}{2} & \text{if } n \text{ is odd} \end{cases}")

if __name__ == "__main__":
    main()
