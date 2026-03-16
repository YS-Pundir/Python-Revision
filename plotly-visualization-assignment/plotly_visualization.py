import pandas as pd
import plotly.express as px

data=pd.DataFrame({
    "Epoch":range(1,11),
    "Loss":[0.99,0.78,0.65,0.23,0.56874,0.45,0.732,0.23,0.45,0.8479]
})

fig=px.line(
    data,
    x=data["Epoch"],
    y=data["Loss"],
    title="Training Loss Over Epochs"  

)

fig.add_annotation(
    x=7,
    y=0.732,
    text="Main Point",
    showarrow=True,
    arrowhead=8,
    arrowcolor="red"
)


fig.show()
fig.write_html("Line_Char.png")