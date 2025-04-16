# pysrc2json
Converts a list of files to JSON for ingestion into a text based LLM

Usage: python program.py <path1> [<path2> ...]"

Example
./program.py ../someproject/src/include/*.h ../someproject/src/*.cpp

Use case:
You can for example document a few classes in Graphviz .dot, paste in the JSON output of a project plus example dot code, and AI can document some class relationships.

It is useful if you forgot to document a project to get you familiar with code base again.


Example graphviz

digraph ClassRelationshipGraph {
    // Defining the central hub class with the interface label
    Server [shape=box, style=filled, color=lightblue, label="Server"];

    // Defining other classes and interfaces
    ServWSHandler [style="filled" fillcolor="darkgreen" fontcolor="white"];
    InferenceHandler [style="filled" fillcolor="darkgreen" fontcolor="white"];
    User [style="filled" fillcolor="darkgreen" fontcolor="white"];
    IServerListener [style="filled" fillcolor="dodgerblue4" fontcolor="white"];
    ServerListener [style="filled" fillcolor="darkgreen" fontcolor="white"];

    // Relationships for Server
    Server -> ServWSHandler [style="dashed", label="composition"];
    Server -> InferenceHandler [style="dashed", label="composition"];
    Server -> ServerListener [style="dashed", label="composition"];

    // Relationships for ServerListener
    ServerListener -> IServerListener [arrowhead="open", style="solid", label="implements"];

    // Relationships for ServWSHandler
    ServWSHandler -> User [style="dotted", label="manages (std::list<shared_ptr>)"];

    // Relationships for User
    User -> "llmwsproto::SessionSetupParamsReqT" [style="dotted", label="holds"];
    User -> "llmwsproto::InferenceReqT" [style="dotted", label="holds"];

    // Relationships for ServWSHandler callback
    ServWSHandler -> IServerListener [style="dashed", label="callback"];

subgraph clusterMain {
  label = "Class Lifetime";
  LifeTime_Per_App [shape=box label="Per\nApp" style="filled" fillcolor="darkgreen" fontcolor="white"];
  LifeTime_Per_User [shape=box label="Per\nUser" style="filled" fillcolor="purple" fontcolor="white"];
  LifeTime_As_Needed [shape=box label="As\nNeeded" style="filled" fillcolor="antiquewhite4" fontcolor="white"];
  Interface_Or_Adapter [shape=box label="Interface\\Adapter" style="filled" fillcolor="dodgerblue4" fontcolor="white"];
  
  // Invisible edges to control layout
  LifeTime_Per_App -> LifeTime_Per_User ->  LifeTime_As_Needed -> Interface_Or_Adapter [style="invis"];

  // Align nodes horizontally
  { rank=same; LifeTime_Per_App, LifeTime_Per_User, LifeTime_As_Needed, Interface_Or_Adapter }
}

}
