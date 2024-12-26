module tutorial/pkg

go 1.23.4

require (
	rsc.io/quote v1.5.2
	tutorial/alias.lib v0.0.0-00010101000000-000000000000
	tutorial/lib v0.0.0-00010101000000-000000000000
)

require (
	golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c // indirect
	rsc.io/sampler v1.3.0 // indirect
)

replace tutorial/lib => ../lib

replace tutorial/alias.lib => ../alias.lib
