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

from fastapi import FastAPI, Request, Query
# ...

@app.post("/generate-plot")
def generate_plot(req: PlotRequest, theme: str = Query("whitegrid")):
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_theme(style=theme)  # 👈 téma alkalmazása

    df = sns.load_dataset(req.dataset)

    plt.clf()
    if req.chartType == "bar":
        sns.barplot(data=df, x=req.x, y=req.y, palette=req.palette)
    elif req.chartType == "violin":
        sns.violinplot(data=df, x=req.x, y=req.y, palette=req.palette)
    elif req.chartType == "box":
        sns.boxplot(data=df, x=req.x, y=req.y, palette=req.palette)
    elif req.chartType == "heatmap":
        sns.heatmap(df.corr(), annot=True, cmap=req.palette)


    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image": f"data:image/png;base64,{img_base64}"}

@app.get("/compare-plot")
def compare_plot():
    df = sns.load_dataset("tips")

    # --- Matplotlib stílusú kép ---
    plt.clf()
    fig, ax = plt.subplots()
    ax.bar(df["day"], df["total_bill"], color="gray")
    ax.set_title("Matplotlib")
    buf1 = io.BytesIO()
    fig.savefig(buf1, format="png")
    buf1.seek(0)
    matplotlib_img = base64.b64encode(buf1.read()).decode("utf-8")

    # --- Seaborn stílusú kép ---
    plt.clf()
    sns.set_theme(style="darkgrid")
    sns.barplot(data=df, x="day", y="total_bill", palette="deep")
    plt.title("Seaborn")
    buf2 = io.BytesIO()
    plt.savefig(buf2, format="png")
    buf2.seek(0)
    seaborn_img = base64.b64encode(buf2.read()).decode("utf-8")

    return {
        "matplotlib": f"data:image/png;base64,{matplotlib_img}",
        "seaborn": f"data:image/png;base64,{seaborn_img}"
    }

