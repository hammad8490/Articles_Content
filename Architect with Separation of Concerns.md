Title: Architect with Separation of Concerns
Slug: architect-with-separation-of-concerns
Tags: MVP Practices, Backend Architecture
Image: architect-with-separation-of-concerns.png
Summary: When constructing the backend architecture for a system, keep the concerns separated. This is a general principle followed in containerized designs, but holds true down to smaller components. Even if the component isn't far away and different, keep responsibilities relegated to separate files or directories.
Date: 2022-01-22 10:00

When constructing the backend architecture for a system, keep the concerns separated. This is a general principle followed in containerized designs, but holds true down to smaller components. Even if the component isn't far away and different, keep responsibilities relegated to separate files or directories.

The most important reason to build this way is interoperability and modularity. You can swap things out when necessary. Oftentimes, requirements grow, and a different library might serve further functionality, so you want to replace an old one. Or maybe you upgrade to a paid service that provides better accuracy or features, so you have to support that instead. By building with this in mind, and keeping each library in its own walled silo, you can swap things in and out with more ease. This leads us to the next point of how these separate components should interface.

In many cases, you want a structured interface between major libraries and components. If you have an ETL or data ingestion process, writing out to an intermediate structure is often best. This can be a file, a database, or data stream like kafka. By doing this, results can be captured later if a downstream event fails or corrupts the data. Otherwise, you can communicate data between services and micro components with an API, though without a playback or recording service, this usually loses replayability / traceability. Either way, a well defined type structured data translation layer is often well advised for communication between services. This can take many forms, depending on the technology stack you're in or the preferred intermediates for the libraries you're using. Protobuf, JSON, yaml, csv, sql, txt are common formats.

<br><br>
There is a lot to keep in mind designing a backend service. Just one important principle is modularity and separation of concerns. Reach out if you need help architecting your MVP.