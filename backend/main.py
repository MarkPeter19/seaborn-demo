from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

# Engedélyezett frontend domain-ek (most bármi jöhet)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlotRequest(BaseModel):
    chartType: str
    dataset: str
    x: str = None
    y: str = None
    palette: str = "deep"

@app.post("/generate-plot")
def generate_plot(req: PlotRequest):
    df = sns.load_dataset(req.dataset)

    plt.clf()
    if req.chartType == "bar":
        sns.barplot(data=df, x=req.x, y=req.y, palette=req.palette)
    elif req.chartType == "violin":
        sns.violinplot(data=df, x=req.x, y=req.y, palette=req.palette)
    elif req.chartType == "heatmap":
        sns.heatmap(df.corr(), annot=True, cmap=req.palette)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image": f"data:image/png;base64,{img_base64}"}
