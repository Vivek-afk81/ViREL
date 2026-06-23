from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional
 

load_dotenv()
model=ChatGroq(model_name="llama-3.3-70b-versatile")

class Schema(TypedDict):
    key_themes:Annotated[list[str],"must write all the key themes discussed in the review in a list"]
    summary:Annotated[str,"must write a brief summary of the review"]
    sentiment:Annotated[str,"must return the sentiment of the review,either positive or Negative"]
    pros:Annotated[Optional[list[str]],"write adown all the pros inside a list"] ## this is optional 
    cons:Annotated[Optional[list[str]],"write adown all the cons inside a list"] ## this is optional 
    
structured_model=model.with_structured_output(Schema)

prompt="""I've been using this phone for about a month, and my experience has been mixed. The display is excellent—bright, smooth, and great for watching videos outdoors. Battery life is another strong point; I can easily get through a full day of heavy use without worrying about charging.

The camera performs well in daylight and captures detailed photos. The design also feels premium for the price, and the phone is comfortable to hold despite its large screen.

However, the software experience is disappointing. There are too many pre-installed apps, and I keep getting notifications from features I never asked for. The interface feels cluttered, and occasional lag makes the phone feel slower than the hardware should allow.

The speakers are average, and low-light camera performance could be better. I also noticed that some apps take longer than expected to open after prolonged use.

Overall, this phone offers great hardware, an excellent display, and strong battery life, but the software experience holds it back. If the manufacturer reduces the bloatware and improves optimization, it would be a much easier recommendation."""

response=structured_model.invoke(prompt)
print(response)