Title: Language Rundown
Slug: language-rundown
Tags: General Info, Programming Language
Image: language-rundown.png
Summary: Choosing the right language for your app is an important decision point for your company. There are nearly infinite strong opinions on each language and which one is best. In this article I'll be as objective as possible and lay out pros and cons for major languages. Most languages are good for a specific use case, and the top few (Python, Node) are often best in most cases.
Date: 2022-01-8 10:00


Choosing the right language for your app is an important decision point for your company. There are nearly infinite strong opinions on each language and which one is best. In this article I'll be as objective as possible and lay out pros and cons for major languages. Most languages are good for a specific use case, and the top few (Python, Node) are often best in most cases.

## Python
Starting with the majority of web apps and backend systems, Python has been the top choice for many years, and still growing. Python is easy to learn and easy to write. This is good to get something down quickly, though can lead to tangled and complex code if not done carefully. Many developers know Python, so it's relatively cheap to build in. Python is a robust language that can handle complex backend systems and modularity. It has some of the highest levels of support and community in its library and integrations. For most backend systems of third parties, if it has something more than a REST interface, it will have Python bindings. Data analysis and ML libraries deserve a special call out, since Python has been king here for years as well. TensorFlow, Pandas, and numpy are major development communities to handle data needs. All in all, Python is a versatile, robust, and cheap option.

## Node.JS
NodeJS is the Javascript server side language. Its greatest strength is in web backends. Javascript might be the most popular language on the internet these days, depending on how you measure. So development is relatively cheap here as well. The way the code is structured with many async callbacks can make reading it reminiscent of spaghetti. However, this weakness is largely its strength as well. Handling asynchronous events, various clicks in unrelated components, and event driven responsiveness is handled best with Node. Sockets and chatting (async usage) is included here. If the frontend is JS heavy, in React, React Native, Angular, or TypeScript, then Node can be a good choice.

## GoLang
GoLang (or just Go) is probably the fastest executing backend language that has most of the modern features and enough popularity to be useful. It also compiles faster than most languages. If you're doing lots of matrix operations, number crunching, or loops, Go can be your best choice. Depending on the IO needs, you can build the computationally intensive component of your app in Go and serve it using a more friendly language. Go was invented at Google and is largely seen as a *readable* language. As a Google engineer, your time is spent mostly reading code, not writing new. This language was built to make it easy to maintain the code. This comes with the tradeoff of being harder to learn and longer to write.

## Ruby on Rails
Ruby on Rails has a very outspoken developer base, and in the early years, had a big rivalry with Python, time has proven that Python is more useful in more situations. Ruby has a lot of short hand, making the code relatively cryptic to non native speakers. But it is a quick prototyping language. There is infrastructure like Heroku that makes it straightforward to deploy apps, though Heroku prices don't scale well.

## .NET
.NET including C#, VB, and F# is an ecosystem of languages from Microsoft. They can be used in server backends as well as other backend processing tasks. Microsoft has its own ecosystem for things, and the library support as well as broad open source support is limited. If your application leans heavily on major pillars of the Microsoft world, whether 360, Windows, etc, the .NET languages can be a good choice.

## C++
C++ is one of the original powerful languages. It is usually the fastest executing language of all. However, over the years, as the language designers continue to add features like templating, the language has become so complex to almost be unusable. It is turing complete in multiple different levels of meta (main language and templating). C++ can be used when you have to eke out every last bit of performance and Go wasn't suitable.

## Swift and Kotlin
Swift and Kotlin are the modern languages to program native apps on iPhone and android respectively. I wrote at more length on native app vs mobile web in another article. These languages are a bit more expensive to develop than the older languages for native apps, and are generally more concise and have more modern features.

## Objective C and Android Java
Objective C and Android Java are the older languages for native apps. These can sometimes have more flexibility than the newer ones, since they are closer to the hardware if some abstractions haven't been fully built out yet for Swift/Kotlin.

## Java
Java runs on the JVM, a virtual machine to run Java code across platforms. It is compiled, and has performance closer to C++ than the interpreted languages. It can be used for heavy computation if you prefer verbose code (not necessarily a bad thing), and dependency injection. It also has robust support for native desktop GUIs in Swing.

## PHP
PHP was the most popular web technology about a decade ago, and as such there are still lots of engineers, usually outsourced, that know it. It has a tendency to get unruly quickly, but there are frameworks like [HACK](https://hacklang.org?ref=mvpengineer.com), from Facebook, that make it better. However, unless you have developers or existing codebase in PHP, it's usually not a good choice to start new.

## HTML and CSS
HTML and CSS are not computer languages in that they are not turing complete and cannot manipulate information in the way others can. They are primarily for displaying information in a pleasing way in the browser. Almost any website will require these languages to display the meat of the website. Sometimes, templating in Jinja or SASS can help, but are not always necessary.

## R
R is a data processing language for statistics. It is mostly used for offline and collaborative processing. Many times, the insights drawn from R analysis are then codified into another language that gets deployed to production. Data scientists will work with the data in R to disentangle and find insights.

## Matlab
Matlab is similar in usecase to R, but has a strong graphing component, and is largely used for matrix analysis. 

## Scala
Scala runs on the JVM, but is a functional language. It has components of object oriented, but is mostly intended to be used in a functional framework. Functional in this context is specific to idempotent functions that operate on data and doesn't effect the underlying data structure. For certain applications, architecting in a functional framework is helpful, and Scala is a readable, popular, and fast executing choice.

## OCaml
OCaml is a mostly functional, strongly typed language used largely in academic settings. It is great to teach CS fundamentals, and is quite clean in its presentation and usage of major concepts. It has limited popularity and commercial use outside of a few specific firms like Jane Street, a market maker.

## LabVIEW
LabVIEW is a specialized graphical language for test and measurement. You can do some general tasks in this language, but you know if you need it. It's largely for test and measurement, when you're using hardware like an oscilloscope or network analyzer. Its major strength is the integrations with these tools.

## Verilog
Verilog, VHDL, and manufacturer specific hardware description languages again you know when you need them. These describe the physical hardware gates that get printed into your demo device. Creating ultra fast execution because your hardware is custom. IOT and wearables will primarily utilize these.

<br><br>
Every language has some pros, and should be used in some cases. Hopefully I've given some considerations for choosing your app's language. Reach out if you want some help scoping and making technical choices on your new initiative.