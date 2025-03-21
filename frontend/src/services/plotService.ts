import type { PlotRequest } from "@/types/plot";

export async function generatePlot(request: PlotRequest): Promise<string> {
  const response = await fetch("http://localhost:8000/generate-plot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  const data = await response.json();
  return data.image; // base64 image string
}
