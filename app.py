import streamlit as st
import altair as alt
url="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
st.title("Illinois Building Inventory")
st.header("Construction Year and Building Size")
scatter=(alt.Chart(url).mark_point(opacity=0.4).encode(x=alt.X("Year Constructed:Q",title="Construction year", scale=alt.Scale(zero=False),),y=alt.Y("Square Footage:Q",title="Square footage(log scale)",scale=alt.Scale(type="log"),),).transform_filter("datum['Year Constructed']>0 && datum['Square Footage']>0"))
dropdown=alt.binding_select(options=["University of Illinois","Department of Corrections", "Department of Natural Resources","Southern Illinois University"],name="Agency: ")
agency=alt.selection_point(fields=["Agency Name"],bind=dropdown)
st.altair_chart(scatter.add_params(agency).transform_filter(agency))

st.write("This scatter plot displays how the building size varies by construction year for the "
    "agency chosen from the drop-down list. Each point is a building. The points are "
    "made partly transparent to make overlapping points easier to see. A logarithmic "
    "scale was used because the square footage of the buildings differs significantly. "
    "With more time, I would include the median square footage for each decade.")
st.header("Total Building Square Footage by Agency")
bars=(alt.Chart(url).mark_bar().encode(x=alt.X("sum(Square Footage):Q", title="Total square footage"),y=alt.Y("Agency Name:N",sort="-x",title="Agency",axis=alt.Axis(labelLimit=350, labelOverlap=False),),).transform_filter("datum['Square Footage']>0").properties(height=760))
st.altair_chart(bars)


st.write( "The above bar graph shows the square footage of buildings in each agency. The top agency is "
    "the University of Illinois with around 25 million square feet of buildings. Then comes the "
    "Department of Corrections with 15 million square feet of buildings. I have used horizontal "
    "bars because the names of the agencies were long. The bars have been arranged in descending "
    "order. This was done to make comparison easier. If I had more time, I would break down each "
    "agency’s total square footage by building type.")
