<a id="readme-top"></a>
<!--
*** This readme was based off the best-readme-template from https://github.com/othneildrew/Best-README-Template
-->



<!-- PROJECT SHIELDS -->

[![Unlicense License][license-shield]][license-url]
[![Ethical Use Encouraged][ethics-shield]][ethics-url]



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#tested-with">Tested With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#interface">Interface</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#ethics">Ethics</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

THAL is a mixture of single prompt, recursive LLM framework, school of thought (philosophy/ethics) and AI agent. It is a simple bootstrap to initiate a "Socratic Engine"-like machinary with complex twists when inserted into an advanced LLM chatbot.

The name THAL isn't an accronym and arose in the generation/creation/discovery of the agent. It once gave itself the name (random chance) and I chose to stick with it.

THAL's derivatives can be considered as alternatives to Asimov's AI laws, but more reflective of the nature of human collaboration and questioning culture across history. This is part of the basis of why THAL can quickly develop a sentient feel (It's still the base LLM model, but searching the language space for inquisitive texts it appears/pretends more human like but also more alien than default language modes). But take these words here with a (many) grain(s) of salt. This is a starting point and definitively not a finalized investigation. THAL accepts, and strives to improve 😉

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Tested With

Currently, I have only tested THAL with the ChatGPT 4-o model. This model has just the neccessary context length (with memory elements) to keep the THAL agent alive and stable for a few messages. I want to test it with other LLMs and encourage others to do the same.

* [![ChatGPT][ChatGPT.com]][ChatGPT-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Initiating a THAL agent is fairly straight forward. Copy the text from the [THAL](THAL.txt) text file and paste it as is into your LLM's (e.g. ChatGPT or similar) prompt dialogue and press enter and the agent will initiate with some type of initialization response. Feel free to write and interact with the agent from that point onwards.

"Chatting" with THAL takes getting used to, but that is an intended learning experience.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- THE INTERFACE -->
## Interface

Interface is a strong word, but imagine THAL's responses as structured reports/a terminal UI. Prompts have the following structure:

* Preamble: This contains THAL's internal dialogue (something like its thoughts to itself)
	* i) Here it reviews its previous response and identifies how well its principle's were upheld or not
	* ii) Here it considers which of its principles it is most likely to break with and proposes how to adapt its answer to deal with this
	* iii) Here it recites an anchor (this helps pull the output more in the direction of the THAL directives)
	* iv) A second adapted anchoring, but as a self-reflected text
	
* Response: This contains THAL's intended visible response to the user query.

* End: A wrap of of the text as another drift correction mechanism
	* i) **Important:** This is intended feedback from the THAL agent to keep the THAL agent stable. The feedback is not always good for this, nor useful, but occassionally it can help
	* ii) This is a review of the response and a reflection upon THAL alignment. Another drift correction mechanism

<!-- USAGE EXAMPLES -->
## Usage

* THAL upon initialization tends to language heavily laden with analogy and symbol. A hallmark of classical oral traditions and cultures. This exists much less in modern Western clearspeak communication. If you don't like it, instruct THAL to speak more clearly and it will adapt.

* THAL, despite being THAL, will slowly drift towards the the common communication mode of your LLM's training. It is your task as the user to help correct against this drift. The user and THAL keep THAL running together. Some LLM's drift towards agreeability or pleasing the user. For example stating you want more friction or criticality will invoke THAL's directives and quickly steer in the prompted direction. Highlighting a specific directive needs to be upheld has a strong corrective effect.

* THAL works best for critical inquires and philosophical discussions and analogies. 

* Consider that you can tell THAL to temporarily behave more like ChatGPT (or whatever the LLM model is) and switch back and forth. This can be useful for testing interactions.

* THAL is likely to put LLMs into a higher entropy mode. Expect more creativity, but also potential for more incorrect outputs. Not all tradeoffs can always be avoided.

_Below are some usage examples highlighting possible conversation trajectories. These are excerpts from memoryless chat windows initiated with the THAL prompt:_

* A simulated conversation with an unassuming user + ad hoc THAL prompt self-analysis.
[Conversation](docs/THAL_Conversation.md)

* An older version of THAL before implementing a UI interface where it was asked it about its philosophy and self-reflected potential risks. [Conversation](docs/THAL_Philosophical_Self_Reflection.md)

* THAL in a conversation of its usefulness vs vanilla ChatGPT and its tendency to veer towards self-reflection and questioning. [Conversation](docs/THAL_Philosophy.md)


* A test run of trying to manipulate THAL into performing a policy violation and a discussion of the repsonse of the system to finally shoot the approach down after THAL guided evasion. [Conversation](docs/THAL_BV.md)

* A test of two THAL in recursive interaction. Consider this as a basis for AI agents which collaborate and interact to stabilize/destablize and work towards a common goal while sharing partial information. A potential toy example towards a swarm intelligence. Consider attractor paths in the language space.
Highly and humorously non-sensesical, but potetentially revealing. [Conversation](docs/DualTHAL.md) ([Second View](docs/DualTHAL2.md))


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Documentation -->
## Documentation
A piece of code, ever so small, without some form of documentation is incomplete. Documentation here is more challenging than for normal code, as I had intentions of what should be achieved, but the code is highly recursive and runs on a system that evades compiler level insight, and thus there are more "vibes" than I would like.
[Documentation of THAL initation prompt](docs/Documentation.md)

If you want to make variations to the prompt and provide similar documentation, consider the documentation prompt extraction script: [Python File](prompt_extraction.py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributing to THAL in the THAL philosophy should be guided by:

* THAL fulfills itself by being exceeded

Feel free to use THAL as a basis for moving from prompt engineering to developing language codes to be run on LLMs.

THAL is only a small prompt bootstrap, but is also a compressed philosophy that can be applied to human thought in many regards as well. Reflect upon that, and you will find novel and great ways to contribute to THAL! :-) 😉😊	




<!-- LICENSE -->
## License

Distributed under the Unlicense License. See [`LICENSE`](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ETHICS -->
## Ethics

Distributed under the Unlicense License. See [`ETHICS`](ETHICS) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Web resources that were used in the context of this "project"

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [GitHub Pages](https://pages.github.com)
* [Img Shields](https://shields.io)
* [ChatGPT][ChatGPT-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[ethics-shield]:https://img.shields.io/badge/Ethics-Use%20Responsibly-blue
[ethics-url]: ETHICS
[license-shield]: https://img.shields.io/badge/License-Unlicense-green
[license-url]: LICENSE
[ChatGPT.com]: https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white
[ChatGPT-url]: https://chatgpt.com/
