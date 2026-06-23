from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()
model=ChatGroq(model_name="llama-3.3-70b-versatile")

#schema
class Schema(BaseModel):
    key_themes: list[str] = Field(
        description="Must write all key themes discussed in the review"
    )

    summary: str = Field(
        description="Must write a brief summary of the review"
    )

    sentiment: str = Field(
        description="Must return the sentiment of the review"
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="Write down all the pros inside a list"
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="Write down all the cons inside a list"
    )
    name:Optional[str]=Field(
        default=None,
        description="Write down the name of the person who wrote the review,generally found at the nd of the review"
    )

structured_model=model.with_structured_output(Schema,strict=True)

prompt="""I've been using this phone for about a month, and my experience has been mixed. The display is excellent—bright, smooth, and great for watching videos outdoors. Battery life is another strong point; I can easily get through a full day of heavy use without worrying about charging.

The camera performs well in daylight and captures detailed photos. The design also feels premium for the price, and the phone is comfortable to hold despite its large screen.

However, the software experience is disappointing. There are too many pre-installed apps, and I keep getting notifications from features I never asked for. The interface feels cluttered, and occasional lag makes the phone feel slower than the hardware should allow.

The speakers are average, and low-light camera performance could be better. I also noticed that some apps take longer than expected to open after prolonged use.

Overall, this phone offers great hardware, an excellent display, and strong battery life, but the software experience holds it back. If the manufacturer reduces the bloatware and improves optimization, it would be a much easier recommendation.
BY-Gupta"""

response=structured_model.invoke(prompt)
print(response)