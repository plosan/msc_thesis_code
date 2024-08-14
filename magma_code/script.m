AttachSpec("IntegralClosureDim2.spec");
Attach("MonomialSequence.m");
prt:=procedure(L)printf"[";for i->l in L do printf"%o%o",l,i lt#L select", "else"]\n";end for;end procedure;




Q<x, y> := LocalPolynomialRing(RationalField(), 2);

/********* INSERT CURVE HERE **********/

//f := (y^2+x^3)^2 + x^5*y;

//f:=(x^4+y^9)^2+x^5*y^7;

f:=(x^3+y^2)^3+x^7*y^2;

//f:=(x^2+y^7)^2+x^5*y^7;
//f:=(x^4+y^9+x^2*y^5)^2+x^5*y^7;


/********* INSERT MAXIMAL CONTACT CURVES HERE **********/

//maxContact := [Q| x, y, y^9+x^4, f ];
// maxContact := [Q| x, y, y^7+x^2, f ];

 maxContact := [Q| x, y, y^2+x^3, f ];



/**************************************/
e := 1;
/**************************************/

/********* NUMBER OF PRIMES ***********/
NP := 1;
/**************************************/

G := SemiGroup(f); g := #G - 1;
E := [i gt 1 select Gcd(Self(i - 1), G[i]) else G[1] : i in [1..#G]];
N := [E[i] div E[i + 1] : i in [1..g]];
V := [N[i]*G[i + 1] : i in [1..g]];

print " ";
print "SemiGroup:", G;
print "Milnor number:", MilnorNumber(G);

print " ";
  print "Yano sets:";
  print "=========================";
  print " ";

  BernsteinSatoGeneric(G);


print " ";
  print "Multiplier Ideals chain";
  print "=========================";
  print " ";






P<x, y> := LocalPolynomialRing(Rationals(), 2, "lglex");

//f:=(x^2+y^7)^2+x^5*y^7;
//maxContact := [P| x, y, y^7+x^2, f ];
//f := (x^4+y^9)^2+x^5*y^7;
//maxContact := [P| x, y, y^9+x^4, f ];
// f := (y^2+x^3)^2 + x^5*y;
f:=(x^3+y^2)^3+x^7*y^2;
maxContact := [P| x, y, y^2+x^3, f ];

 Mult := MultiplierIdeals(f);
 // printf "#Mult = %o\n", #Mult;


 for e in Mult do
      S, jn := Explode(e);
      printf "JN = %o\n", jn;
      SNice, extras := MonomialSequence(S, maxContact);
      // printf "SNice = %o\n\n", SNice;
      // printf "extras = %o\n\n", extras;
      printf "Ideal = "; prt(SNice);
      printf "\n";
      for i->e in extras do
           printf "g%o = %o\n", i, e;
      end for;
 end for;


print " ";
  print "Rupture Filtration chain 1";
  print "=========================";
  print " ";

// // JJ := TjurinaFiltration(f);
// // print JJ;

  JJ := FiltrationRupture(f, 1);
 //print JJ;
 //printf "# = %o\n", #JJ;


 for e in JJ do
      S, n := Explode(e);
     ChangeUniverse(~S, P);
      printf "%o\n", n;
      SNice, extras := MonomialSequence(S, maxContact);
      // printf "SNice = %o\n\n", SNice;
      // printf "extras = %o\n\n", extras;
      printf "Ideal = "; prt(SNice);
      printf "\n";
      for i->e in extras do
           printf "g%o = %o\n", i, e;
      end for;
 end for;

print " ";
  print "Rupture Filtration chain 2";
  print "=========================";
  print " ";

 JJ := FiltrationRupture(f, 2);
 // JJ := FiltrationRupture(f, 1);
 //print JJ;
 //printf "# = %o\n", #JJ;


 for e in JJ do
      S, n := Explode(e);
     ChangeUniverse(~S, P);
      printf "%o\n", n;
      SNice, extras := MonomialSequence(S, maxContact);
      // printf "SNice = %o\n\n", SNice;
      // printf "extras = %o\n\n", extras;
      printf "Ideal = "; prt(SNice);
      printf "\n";
      for i->e in extras do
           printf "g%o = %o\n", i, e;
      end for;
 end for;



















// // R<t,u> := RationalFunctionField(RationalField(),2);
// // P<x, y> := LocalPolynomialRing(R, 2, "lglex");
// // P<x, y> := LocalPolynomialRing(RationalField(), 2, "lglex");
// P<x, y> := LocalPolynomialRing(FiniteField(31), 2, "lglex");
// // P<x, y> := PolynomialRing(RationalField(), 2);
// // f1 := (y^2-x^3);
// // f2 := (y^2-x^3)^4 + x^8*y^5;
// // maxContact := [x, y, f1, f2];
// // S := [P|
// //      2,
// //      x,
// //      y,
// //      f1,
// //      f2,
// //      -5*f1,
// //      -5*f1^2*f2,
// //      f1*(x+3*y^2)*(x*y-1),
// //      f1^2*(3*x+y^2)^3
// // ];
// // I := ideal<P| S >;

// maxContact := [P| y^2+x^3, (y^2+x^3)^5 + x^3*y^10 ];
// S := [P|
// x*y^9,x^2*y^9,x^3*y^8,x^4*y^7,x^5*y^6+x^2*y^8,x^6*y^5+2*x^3*y^7+y^9,x^7*y^5,x^8*y^4-x^2*y^8,x^9*y^3-3*x^3*y^7-2*y^9,x^10*y^2+3*x^7*y^4+3*x^4*y^6+x*y^8,x^12*y+4*x^3*y^7+3*y^9,x^13-6*x^7*y^4-8*x^4*y^6-3*x*y^8
// ];


// ////////////////////


// printf "\n";
// // printf "S = %o\n\n", S;
// SNice, extras := MonomialSequence(S, maxContact);
// // printf "SNice = %o\n\n", SNice;
// // printf "extras = %o\n\n", extras;
// printf "Ideal = "; prt(SNice);
// printf "\n";
// for i->e in extras do
//      printf "g%o = %o\n", i, e;
// end for;
// // printf "extras = "; prt(extras);

// // // printf "----------"^5 cat "\n\n";
// // printf "\n";

// // // printf "I = %o\n\n", I;
// // SNice, extras := MonomialSequence(I, maxContact);
// // // printf "SNice = %o\n\n", SNice;
// // // printf "extras = %o\n\n", extras;
// // printf "SNice = "; prt(SNice);
// // printf "extras = "; prt(extras);

// // // MonomialSequence;




// print "\n";
// print "-------------------------------------------------\n";
// print "\n";






//print " ";
//  print "Nu Filtration chain";
//  print "=========================";
//  print " ";

// JJ := NuFiltration(f, 13);
// print JJ;
// printf "# = %o\n", #JJ;




// print " ";
 // print "Nu Filtration Rupture chain";
 //  print "=========================";
//  print " ";

// p:=13;
// KK1 := NuFiltrationRupture(f, 1, 13);
// print [<nu[1], nu[1]/(p-1)> : nu in NuFiltrationRupture(f, 1, p)];
//print KK1;
// printf "# = %o\n", #KK1;

// print " ";

// p:=53;
// KK2 := NuFiltrationRupture(f, 2, p);
 // print [<nu[1], nu[1]/(p-1)> : nu in NuFiltrationRupture(f, 2, p)];
// print KK2;
// printf "# = %o\n", #KK2;

// print " ";

// p:=11;
// KK1 := NuFiltrationRupture(f, 1, p);
 // print [<nu[1], 1-(nu[1]+1)/(p+1), 2-(nu[1]+2)/(p+1)> : nu in NuFiltrationRupture(f, 2, p)];
// print KK2;
// printf "# = %o\n", #KK2;

// print " ";

// p:=103;
// KK2 := NuFiltrationRupture(f, 2, p);
// print [<nu[1], 1-(nu[1]+1)/(p+1), 2-(nu[1]+2)/(p+1)> : nu in NuFiltrationRupture(f, 2, p)];
// print KK2;
//printf "# = %o\n", #KK2;







///// For each rupture point.... ///////
for i in [1..g] do
/********* NUMBER TO MOD OUT BY **********/
  v := N[i]*G[i + 1];
/*****************************************/

  print " ";
  print "Rupture point value:", v;
  print "=========================";
  print " ";

  /////////////////////////////////////////
  ////////// p = +1 mod v /////////////////
  /////////////////////////////////////////
  print "Primes congruent +1 mod ", v;
  print "-----------------------------";
  print " ";

/*********** INITIAL PRIME ***************/
  p := 3;
/*****************************************/
  for j in [1..NP] do
    while not IsPrime(p) or p mod v ne 1 do p +:= 2; end while;
    print "Nu invariants with p =", p, ":";
// print [FiltrationRupture(f,i)];

print " ";
  print "lambda";
  print "---------------";
  print " ";
    print [<nu[1], nu[1]/(p-1)> : nu in NuFiltrationRupture(f, i, p)];
    //print [<nu[1], nu[2], nu[1]/(p-1)> : nu in NuFiltrationRupture(f, i, p)];
// print NuFiltrationRupture(f, i, p : e := e, N := v);

// <===========================================

 print " ";
  print "e-th-root chain";
  print "=========================";
  print " ";



    R<x, y> := PolynomialRing(FiniteField(p), 2);


    maxContact := [R| x, y, y^2+x^3, f ];

    //maxContact := [R| x, y, y^9+x^4, f ];

    C := ethRootChain(ideal<R | f>, 1);
    print "Num. ideals in the eth-root chain with p =", p, ":", #C;
    print "Jumps in th eth-root chain with p =", p, ":";
    print [c[2] : c in C]; print "\n";
    p +:= 2;
  end for;



  for e in C do
      S, n := Explode(e);
     ChangeUniverse(~S, R);
      printf "%o\n", n;
      SNice, extras := MonomialSequence(S, maxContact);
      // printf "SNice = %o\n\n", SNice;
      // printf "extras = %o\n\n", extras;
      printf "Ideal = "; prt(SNice);
      printf "\n";
      for i->e in extras do
           printf "g%o = %o\n", i, e;
      end for;
 end for;





  /////////////////////////////////////////
  ////////// p = -1 mod v /////////////////
  /////////////////////////////////////////
  print "\n";
  print "Primes congruent -1 mod ", v;
  print "-----------------------------";
  print " ";

/*********** INITIAL PRIME ***************/
  p := 3;
/*****************************************/
  for j in [1..NP] do
    while not IsPrime(p) or p mod v ne v - 1 do p +:= 2; end while;
    print "Nu invariants with p =", p, ":";
    //print [FiltrationRupture(f,i)];
   // print [<nu[1], nu[2], 1-(nu[1]+1)/(p+1), 2-(nu[1]+2)/(p+1)> : nu in NuFiltrationRupture(f, i, p)];
  //  print [<nu[1], 1-(nu[1]+1)/(p+1), 2-(nu[1]+2)/(p+1)> : nu in NuFiltrationRupture(f, i, p)];

 print " ";
  print "1-lambda";
  print "---------------";
  print " ";
 print [<nu[1], 1-(nu[1]+1)/(p+1)> : nu in NuFiltrationRupture(f, i, p)];
 print " ";
  print "2-lambda";
  print "---------------";
  print " ";
 print [<nu[1], 2-(nu[1]+2)/(p+1)> : nu in NuFiltrationRupture(f, i, p)];
// print NuFiltrationRupture(f, i, p : e := e, N := v);

//<===========================================

 print " ";
  print "e-th-root chain";
  print "=========================";
  print " ";


    R<x, y> := PolynomialRing(FiniteField(p), 2);

//maxContact := [R| x, y, y^9+x^4, f ];
maxContact := [R| x, y, y^2+x^3, f ];

    C := ethRootChain(ideal<R | f>, 1);
    print "Num. ideals in the eth-root chain with p =", p, ":", #C;
    print "Jumps in th eth-root chain with p =", p, ":";
    print [c[2] : c in C]; print "\n";
    p +:= 2;
  end for;

    for e in C do
      S, n := Explode(e);
     ChangeUniverse(~S, R);
      printf "%o\n", n;
      SNice, extras := MonomialSequence(S, maxContact);
      // printf "SNice = %o\n\n", SNice;
      // printf "extras = %o\n\n", extras;
      printf "Ideal = "; prt(SNice);
      printf "\n";
      for i->e in extras do
           printf "g%o = %o\n", i, e;
      end for;
 end for;

  print "\n";  print "------------------------------------------------------------";
end for;
