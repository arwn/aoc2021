let input = System.IO.File.ReadLines("input_1")
            |> Seq.toArray
            |> Array.map int

let countIncreases xs = 
    xs
    |> Seq.pairwise
    |> Seq.map (fun (l,r) -> l < r)
    |> Seq.sumBy (fun b -> if b then 1 else 0)

let answer =
    countIncreases input

printfn "%A" answer

let answer2 =
    let extended = Array.append input [|0;0|]
    Array.mapi (fun i x -> extended.[i..i+2]) input
    |> Array.map Array.sum
    |> countIncreases

printfn "%A" answer2